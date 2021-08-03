t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    res = 0
    temp = 0
    for a in A:
        temp += a
        res = min(res, temp)
    print(-res)
