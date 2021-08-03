t = int(input())
for i in range(t):
    n = int(input())
    mi = 10**100
    ma = 0
    for j in range(n):
        a, b = [int(x) for x in input().split()]
        mi = min(mi, b)
        ma = max(a, ma)
    print(max(ma - mi, 0))
