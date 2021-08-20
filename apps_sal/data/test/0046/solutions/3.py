(n, m) = map(int, input().split())
a = [n // 5 + (n % 5 > i) for i in range(5)]
b = [m // 5 + (m % 5 > i) for i in range(5)]
ans = 0
for i in range(4):
    ans += a[i] * b[3 - i]
print(ans + a[4] * b[4])
