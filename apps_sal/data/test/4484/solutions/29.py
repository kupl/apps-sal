n, m = map(int, input().split())

if abs(n-m) >= 2:
    print(0)
    return

ans = 1
div = 10**9+7

for i in range(1, n+1):
    ans = (ans * i) % div
for i in range(1, m+1):
    ans = (ans * i) % div

if n != m:
    print(ans)
else:
    print((ans*2)%div)
