a = int(input())
b = [int(x) for x in input().split()]
c = [b[0]]
for i in b[1:]:
    if i != c[-1]:
        c.append(i)
a = len(c)

dpa = []
dpb = [0] * (a + 1)
for i in range(2, a + 1):
    dp = []
    for j in range(a - i + 1):
        if c[j] == c[j + i - 1]:
            dp.append(min(dpb[j], dpb[j + 1], dpa[j + 1]) + 1)
        else:
            dp.append(min(dpb[j], dpb[j + 1]) + 1)
    dpa, dpb = dpb, dp
print(dpb[0])
