t = int(input())
for i in range(t):
    a, b, x, y = list(map(int, input().split()))
    print(max(x * b, y * a, (a - x - 1) * b, (b - y - 1) * a))
