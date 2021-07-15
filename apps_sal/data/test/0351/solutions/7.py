n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a = list(sorted(a))
d = k
ans = 0
for ai in a:
    while 2 * d < ai:
        d *= 2
        ans += 1
    d = max(d, ai)

print(ans)

