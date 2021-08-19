# B Golden Apple
n, d = list(map(int, input().split()))
deco = d * 2 + 1
if n % deco == 0:
    print((n // deco))
else:
    print(((n // deco) + 1))
