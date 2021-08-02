n, x, t = map(int, input().split())
for i in range(n * t + 1):
    if x * i >= n:
        print(i * t)
        break
