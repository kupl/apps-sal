t = int(input())
for _ in range(t):
    a, b, x, y = map(int, input().split())
    print(max([x * b, (a - x - 1) * b, a * y, a * (b - y - 1)]))
