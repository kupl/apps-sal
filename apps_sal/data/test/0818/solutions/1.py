n = int(input())
k = True
if n < 3:
    print(-1)
    k = False
if k:
    x = 10 ** (n - 1)
    while x % 210 != 0:
        x += 1
    print(x)
