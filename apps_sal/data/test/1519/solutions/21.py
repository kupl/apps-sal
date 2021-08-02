n, L, a = [int(x) for x in input().split()]
pr = 0
ans = 0
for i in range(n):
    t, l = [int(x) for x in input().split()]
    if t >= pr + a:
        ans += abs(pr - t) // a
    pr = t + l
ans += (L - pr) // a
print(ans)
