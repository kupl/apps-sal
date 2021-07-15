n, m, k = map(int, input().split())
t1 = 2 * m
ps1 = (k - 1) // t1 + 1
ps2 = (k % t1)
if ps2 == 0:
    ps2 = 2 * m
print(ps1, (ps2 + ps2 % 2) // 2, ("L" if ps2 % 2 == 1 else "R"))
