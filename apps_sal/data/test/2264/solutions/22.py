t = int(input())
for i in range(t):
    n = int(input())
    ll = 0
    rr = 1000000001
    for j in range(n):
        l, r = list(map(int, input().split()))
        rr = min(r, rr)
        ll = max(l, ll)
    print(max(0, ll - rr))
