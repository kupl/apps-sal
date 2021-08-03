def GCD(x, y):
    while (x != y):
        if x < y:
            x, y = y, x
        x -= y
    return x


n = int(input())
ar = list(map(int, input().split(' ')))
r = ar[0]
for i in range(n - 1):
    r = GCD(r, ar[i + 1])
print(r * n)
