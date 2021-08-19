def get2(n):
    res = n * (n + 1) * (2 * n + 1) // 6 + n * (n + 1) // 2
    res //= 2
    return res


def get(x, y):
    return get2(x + y) - get2(x - 1) - get2(y - 1)


(m, b) = input().split()
m = int(m)
b = int(b)
mv = 0
for i in range(b + 1):
    j = m * b - m * i
    cur = get(j, i)
    if cur > mv:
        mv = cur
print(mv)
