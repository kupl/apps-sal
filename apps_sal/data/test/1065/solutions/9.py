import math
(n, k, M, D) = input().split()
n = int(n)
k = int(k)
M = int(M)
D = int(D)
ans = -1
for a in range(1, D + 1):
    r = a * k
    l = (a - 1) * k + 1
    l1 = math.ceil(n / (r + 1))
    if l > 0:
        r1 = n // l
    else:
        r1 = 999999999999999999
    if r1 >= l1 and M >= l1:
        x = min(r1, M)
        ans = max(ans, x * a)
print(ans)
