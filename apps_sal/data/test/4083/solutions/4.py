from sys import stdin

input = stdin.readline
inf = 1000 * 1000 * 1000

n, k = list(map(int, input().split()))
a = [int(i) for i in input().split()]

a.sort()
res = inf
for i in range(0, 200001, 1):
    b = []
    for j in a:
        tmp2 = 0
        while j > i:
            tmp2 += 1
            j //= 2
        if j == i:
            b.append(tmp2)
        else:
            b.append(inf)
    b.sort()
    tmp = 0
    for i in range(k):
        tmp += b[i]
    res = min(res, tmp)

print(res)

