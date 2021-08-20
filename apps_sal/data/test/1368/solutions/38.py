from collections import Counter
from math import factorial
(N, A, B) = list(map(int, input().split()))
V = list(map(int, input().split()))
C = Counter(V)
keys = list(C.keys())
keys.sort(reverse=True)
if C[keys[0]] >= A:
    mean = keys[0]
    var = 0
    for i in range(A, min(B, C[keys[0]]) + 1):
        var += factorial(C[keys[0]]) // factorial(i) // factorial(C[keys[0]] - i)
else:
    cnt = 0
    total = 0
    var = 0
    for v in keys:
        if cnt + C[v] < A:
            cnt += C[v]
            total += v * C[v]
        else:
            total += v * (A - cnt)
            mean = total / A
            var += factorial(C[v]) // factorial(A - cnt) // factorial(C[v] - (A - cnt))
            break
print(mean)
print(var)
