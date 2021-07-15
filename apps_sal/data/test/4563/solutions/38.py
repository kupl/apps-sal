n = int(input())
t, a = map(int, input().split())
for _ in range(n - 1):
    x, y = map(int, input().split())
    s = max((t + x - 1) // x, (a + y - 1) // y)
    t, a = s * x, s * y
print(t + a)
