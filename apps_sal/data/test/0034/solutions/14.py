(n, a, b) = list(map(int, input().split()))
for i in range(200, 0, -1):
    if a // i > 0 and b // i > 0 and (a // i + b // i >= n):
        print(i)
        break
