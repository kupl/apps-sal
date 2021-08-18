import math
from collections import Counter
n, a, b = map(int, input().split())
lists = list(map(int, input().split()))
lists = sorted(lists)
P = sum(lists[-a:])
print(P / a)
J = dict(Counter(lists))
K = dict(Counter(lists[-a:]))
ans = 1
sums = 0
if J[max(lists)] < a:
    for some in K.keys():
        ans *= (math.factorial(J[some]) // ((math.factorial(K[some])) * math.factorial(J[some] - K[some])))
    print(ans)
elif J[max(lists)] > a:
    for i in range(a, min(b, J[max(lists)]) + 1):
        sums += math.factorial(J[max(lists)]) // (math.factorial(J[max(lists)] - i) * math.factorial(i))
    print(sums)
else:
    print(1)
