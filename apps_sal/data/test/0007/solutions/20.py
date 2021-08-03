n, m = [int(x) for x in input().split()]
if (m >= n):
    print(n)
    return
L = m
R = n
while (L + 1 < R):
    M = (L + R) // 2
    z = M - m
    if (z * (z - 1) // 2 + M >= n):
        R = M
    else:
        L = M
print(R)
