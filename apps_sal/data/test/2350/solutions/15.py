import sys
t = int(input())

for _ in range(t):
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    dx = x2 - x1
    dy = y2 - y1
    print(dx * dy + 1)

return
arr = [[0] * 1000 for _ in range(1000)]
sets = [[set() for _ in range(1000)] for _ in range(1000)]

c = 1
for i in range(1, 200):
    for j in range(i):
        arr[j][i - j - 1] = c
        c += 1

print(*[r[:20] for r in arr[:20]], sep="\n")

sets[0][0].add(arr[0][0])

for x in range(20):
    for y in range(20):
        v = arr[x][y]
        if x > 0:
            sets[x][y] = sets[x][y] | sets[x - 1][y]
        if y > 0:
            sets[x][y] = sets[x][y] | sets[x][y - 1]
        sets[x][y] = set([v + val for val in sets[x][y]])

print(*[[len(s) for s in r[:20]] for r in sets[:20]], sep="\n")
