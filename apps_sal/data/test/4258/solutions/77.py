a, b, t = map(int, input().split())
ans = 0
nt = 0
while(nt + a <= t):
    nt += a
    ans += b
print(ans)
