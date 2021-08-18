from copy import deepcopy
from itertools import product
n, a, b, c, *L = map(int, open(0).read().split())
L.sort(reverse=True)

li1 = [4, 1, 2, 3]
ans = 10**10
for v in product(li1, repeat=n):
    num = 0
    A, B, C, NO = [], [], [], []
    for i in range(n):
        if v[i] == 1:
            A.append(L[i])
        elif v[i] == 2:
            B.append(L[i])
        elif v[i] == 3:
            C.append(L[i])
        elif v[i] == 4:
            NO.append(L[i])
    if A and B and C:
        num += abs(sum(A) - a) + max(0, (len(A) - 1) * 10) + abs(sum(B) - b) + max(0, (len(B) - 1) * 10) + abs(sum(C) - c) + max(0, (len(C) - 1) * 10)
        ans = min(ans, num)
print(ans)
