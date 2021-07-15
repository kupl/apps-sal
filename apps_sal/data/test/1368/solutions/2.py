import math
from collections import Counter
N, A, B = list(map(int, input().split()))
V = list(map(int, input().split()))

V.sort(reverse=True)
c = Counter(V)
L = []
for i in range(A, B + 1):
    L.append(sum(V[0:i]) / i)

ans = []
for i in range(A, B + 1):
    c_t = Counter(V[0:i])
    tmp = 1
    for k, v in list(c_t.items()):
        tmp *= math.factorial(c[k]
                              ) // math.factorial(v) // math.factorial(c[k] - v)
    ans.append(tmp)

max_L = max(L)

num = 0
for i in range(len(L)):
    if L[i] == max_L:
        num += ans[i]

print(('{:.6f}'.format(max_L)))
print(num)

