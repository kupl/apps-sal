n = int(input())
a = 10000000000
a1 = -10000000000
for i in range(n):
    x, y = map(int, input().split())
    a = min(a, y)
    a1 = max(a1, x)
m = int(input())
b = -10000000000
b1 = 10000000000
for i in range(m):
    x, y = map(int, input().split())
    b = max(b, x)
    b1 = min(b1, y)
print(max(0, b - a, a1 - b1))
