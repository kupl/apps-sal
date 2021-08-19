n = int(input())
cards = list(map(int, input().split()))

score = 0
preIndexes = []
nextIndexes = []
isChosen = [0] * n
chosens = []

# first card score initialize
nextIndexes.append(1)
preIndexes.append(-1)

for i in range(1, n - 1):
    if cards[i] <= cards[i - 1] and cards[i] <= cards[i + 1]:
        chosens.append((-cards[i], i))
        isChosen[i] = 1
    preIndexes.append(i - 1)
    nextIndexes.append(i + 1)

# last card score initialize
preIndexes.append(n - 2)
nextIndexes.append(n)

while len(chosens) != 0:
    chosen = chosens.pop()
    preChosen = preIndexes[chosen[1]]
    nextChosen = nextIndexes[chosen[1]]

    # handle score
    score += min(cards[preChosen], cards[nextChosen])

    # handle deleting
    nextIndexes[preChosen] = nextChosen
    preIndexes[nextChosen] = preChosen

    # check if preChosen can be chosen
    if preChosen != 0 and preIndexes[preChosen] != -1 and nextIndexes[preChosen] != n:
        if cards[preChosen] <= cards[preIndexes[preChosen]] and cards[preChosen] <= cards[nextIndexes[preChosen]]:
            if isChosen[preChosen] == 0:
                isChosen[preChosen] = 1
                chosens.append((-cards[preChosen], preChosen))
    # check if nextChosen can be chosen
    if nextChosen != n - 1 and preIndexes[nextChosen] != -1 and nextIndexes[nextChosen] != n:
        if cards[nextChosen] <= cards[preIndexes[nextChosen]] and cards[nextChosen] <= cards[nextIndexes[nextChosen]]:
            if isChosen[nextChosen] == 0:
                isChosen[nextChosen] = 1
                chosens.append((-cards[nextChosen], nextChosen))

tempNode = nextIndexes[0]
while tempNode != n and tempNode != n - 1:
    score += min(cards[preIndexes[tempNode]], cards[nextIndexes[tempNode]])
    tempNode = nextIndexes[tempNode]

print(score)
