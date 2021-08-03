t = int(input())
for q in range(0, t):
    x, y = list(map(int, input().split()))
    a, b = list(map(int, input().split()))
    print(min(b * min(x, y) + a * (max(x, y) - min(x, y)), (x + y) * a))
