(n, l, r) = [int(s) for s in input().split()]
(m1, m2) = (0, 0)
i = 1
(L, R) = (2 ** l, 2 ** r)
m1 = L - 1
m2 = R - 1
m1 += n - l
m2 += (n - r) * R // 2
print(m1, m2)
