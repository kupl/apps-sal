n, a, b = list(map(int, input().split()))
for x in range(1, 110):
    if a // x + b // x < n or a < x or b < x:
        print(x - 1)
        break
