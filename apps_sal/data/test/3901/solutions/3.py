from math import gcd
n = int(input())
arr = list(map(int, input().split()))
ones = arr.count(1)
if ones > 0:
    print(n - ones)
else:
    gcds = [[0] * n for i in range(n)]
    for i in range(n):
        gcds[i][i] = arr[i]
    seglen = 10000
    for i in range(n + 1):
        for j in range(i + 1, n):
            gcds[i][j] = gcd(gcds[i][j - 1], arr[j])
            if gcds[i][j] == 1:
                seglen = min(seglen, j - i + 1)
    if seglen == 10000:
        print(-1)
    else:
        makeone = seglen - 1
        ones = 1
        res = makeone + n - ones
        print(res)
