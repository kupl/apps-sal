from collections import OrderedDict

A, B, K = map(int, input().split())
L = []
res = []

if K > B-A:
    for i in range(A, B+1):
        print(i)
    return
else:
    for i in range(A, A+K):
        res.append(i)
    for i in range(B-K+1, B+1):
        res.append(i)

res_unique = list(set(res))
res_unique.sort()

for i in res_unique:
    print(i)
