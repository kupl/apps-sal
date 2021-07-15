
t = int(input())
for i in range(t):
    n = int(input())
    cards = list()
    cou = 0
    for j in range(n):
        cards.append(input())
    br = False
    for j in range(n):
        br = False
        if cards.count(cards[j]) > 1:
            for k in range(4):
                for m in range(10):
                    temp = list(cards[j])
                    temp[k] = str(m)
                    temp = "".join(temp)
                    if temp not in cards:
                        cards[j] = temp
                        cou += 1
                        br = True
                        break
                if br:
                    break
    print(cou)
    print(*cards, sep="\n")

