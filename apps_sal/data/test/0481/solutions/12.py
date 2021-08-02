n, x = map(int, input().split(' '))
c = 0
for i in range(1, n + 1):
    d = x // i
    m = x % i
    if d <= n and m == 0:
        c += 1
print(c)
