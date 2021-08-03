n = int(input())
a = [int(input()) for i in range(n)]

p, q = 0, 0
judge = 1000
for v in a:
    if v % 10:
        p += v
        judge = min(judge, v)
    else:
        q += v

ans = p + q
if ans % 10 == 0:
    if judge == 1000:
        ans = 0
    else:
        ans -= judge

print(ans)
