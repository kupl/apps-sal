n = int(input())
s = []
for i in range(n):
    a, b = map(int, input().split())
    s.append((b - a, a, b))
s.sort()
ans = 0
for i in range(n):
    d, a, b = s[i]
    ans += a * i + b * (n - i - 1)
print(ans)
