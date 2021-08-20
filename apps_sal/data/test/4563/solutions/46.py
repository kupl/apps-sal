n = int(input())
a = b = 1
for i in range(n):
    (x, y) = map(int, input().split())
    m = max(int((a - 1) // x) + 1, int((b - 1) // y) + 1)
    a = m * x
    b = m * y
print(a + b)
