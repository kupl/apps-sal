n = int(input())
m = 10 ** 13
for x in range(1, 1000001):
    y = n / x
    if y % 1 == 0:
        v = x + y - 2
        m = min(m, v)
print(int(m))
