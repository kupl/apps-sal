n, b, d = list(map(int, input().split()))
a = list(map(int, input().split()))
dd = 0
ans = 0
for ai in a:
    if ai<=b:
        dd += ai
    if dd > d:
        ans += 1
        dd = 0
print(ans)

