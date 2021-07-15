n = int(input())
i = 1
ans = 0
while i * i <= n:
    if n % i == 0:
        ans += 2
    i += 1
i -= 1
if i * i == n:
    ans -= 1
print(ans)
