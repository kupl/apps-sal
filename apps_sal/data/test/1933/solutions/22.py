h, w, k = map(int, input().split())
d = [[int(x) for x in input().split()] for _ in range(h)]
d = [[x for x in line] for line in zip(*d)]

totalScore = 0
totalCost = 0

for line in d:
    max = 0
    cost = 0
    cur = 0
    curCost = 0
    for c1, c2 in zip(line, [0] * k + line):
        cur += c1
        cur -= c2
        curCost += c2
        if cur > max:
            cost = curCost
            max = cur
    totalScore += max
    totalCost += cost

print(totalScore, totalCost)
