N = int(input())
(a, b) = (1, 1)
for i in range(N):
    (x, y) = map(int, input().split())
    n = max((a + x - 1) // x, (b + y - 1) // y)
    a = n * x
    b = n * y
print(a + b)
