TC = int(input())
for _ in range(TC):
    (a, b, x, y) = list(map(int, input().split()))
    print(max(y * a, x * b, (b - y - 1) * a, (a - x - 1) * b))
