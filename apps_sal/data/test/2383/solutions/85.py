(n, a, b) = (int(input()), [*map(int, input().split())], 1)
for i in range(n):
    if b == a[i]:
        b += 1
print([n - b + 1, -1][b == 1])
