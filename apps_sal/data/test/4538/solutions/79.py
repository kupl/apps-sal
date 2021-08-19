(n, d) = list(map(int, input().split()))
c = 0
for _ in range(n):
    (x, y) = list(map(int, input().split()))
    if (x ** 2 + y ** 2) ** 0.5 <= d:
        c += 1
print(c)
