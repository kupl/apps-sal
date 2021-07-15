r, h = list(map(int, input().split()))
a = 1 + 2 * h // r
if h % r >=3 ** 0.5 * r / 2:
    a += 1
print(a)

