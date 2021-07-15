t = int(input())
for _ in range(t):
    x, y, k = map(int, input().split())
    n = (k * (y + 1) - 1 + (x - 2)) // (x - 1)
    print(n + k)
