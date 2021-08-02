n, k = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n)]
res = k
ab.sort()
for i in range(n):
    res -= ab[i][1]
    if res <= 0:
        print(ab[i][0])
        return
