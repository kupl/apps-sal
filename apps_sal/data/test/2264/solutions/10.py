t = int(input())
for i in range(t):
    n = int(input())
    (maxl, minr) = list(map(int, input().split()))
    for j in range(1, n):
        (l, r) = list(map(int, input().split()))
        maxl = max(l, maxl)
        minr = min(r, minr)
    print(max(maxl - minr, 0))
