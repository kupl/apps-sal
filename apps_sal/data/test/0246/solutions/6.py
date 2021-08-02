n, s = map(int, input().split())

ans = 0
p = s
for i in range(163):
    p = s + i
    if p > n:
        break
    if p >= s + sum(map(int, str(p))):
        ans += 1

if p <= n:
    ans += n - p

print(ans)
