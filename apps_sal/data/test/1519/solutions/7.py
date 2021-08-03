n, l, a = list(map(int, input().split()))
ans = 0
if n > 0:
    lt, ltt = 0, 0

    for i in range(n):
        t, tt = list(map(int, input().split()))
        ans += (t - (lt + ltt)) // a
        lt, ltt = t, tt
    ans += (l - (lt + ltt)) // a
else:
    ans += l // a

print(ans)
