n = int(input())
a = 0
b = 0
for i in range(1, n + 1):
    a += (n - i + 1) * (n - i + 2) // 2
for i in range(n - 1):
    u, v = map(int, input().split())
    b += min(u, v) * (n - max(u, v) + 1)
print(a - b)
