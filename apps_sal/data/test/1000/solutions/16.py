n, v = [int(item) for item in input().split()]

x = 0
c = 0
for i in range(1, n):
    if x < n - i:
        c += i * min((n - i), v - x)
        x += min((n - i), v - x)
    x -= 1

print(c)
