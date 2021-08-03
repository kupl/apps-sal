n = int(input())
f = list(map(int, input().split()))
f.sort(reverse=True)
ans = 0
if n % 2 == 0:
    for i in range(n // 2):
        ans += f[i] * 2
    ans -= f[0]
else:
    for i in range(n // 2):
        ans += f[i] * 2
    ans += f[n // 2] - f[0]

print(ans)
