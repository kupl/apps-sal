n = int(input())

ans = 0
for i in range(1, n + 1):
    ans += i * (n - i + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    ans -= a * (n - b + 1)

print(ans)
