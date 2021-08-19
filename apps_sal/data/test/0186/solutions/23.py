nm = input().split(" ")
n = int(nm[0])
m = int(nm[1])
# not allowed to be the same height, not not same number of blocks
if n == 0:
    print(3 * m)
elif m == 0:
    print(2 * n)
else:
    new = max(3 * m, 2 * n)
    i = 0
    while i < new + 1:
        if i % 6 == 0 and i != 0:
            if i // 3 <= m and i // 2 <= n and 2 * (n + 1) - new < 3 * (m + 1) - new:
                n += 1
            elif i // 3 <= m and i // 2 <= n and 2 * (n + 1) - new >= 3 * (m + 1) - new:
                m += 1
            new = max(3 * m, 2 * n)
        i += 1
    print(max(3 * m, 2 * n))
