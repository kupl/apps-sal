n = int(input())
(a, b) = map(int, input().split())
for i in range(n - 1):
    (c, d) = map(int, input().split())
    x = -min(-a // c, -b // d)
    (a, b) = (c * x, d * x)
print(a + b)
