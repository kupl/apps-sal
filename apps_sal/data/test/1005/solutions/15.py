t = int(input())
for _ in range(t):
    (n, k, d) = map(int, input().split())
    a = list(map(int, input().split()))
    res = d
    for i in range(n - d + 1):
        res = min(res, len(set(a[i:d + i])))
    print(res)
