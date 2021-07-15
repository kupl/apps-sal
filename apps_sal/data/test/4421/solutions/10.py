from collections import Counter as C
n, k = map(int, input().split())
l = [int(x) % k for x in input().split()]
c = C(l)
res = 0
for i in range(k):
    j = -i % k
    vi, vj = c.get(i, 0), c.get(j, 0)
    if i == j:
        res += vi // 2
    else:
        res += min(vi, vj)
    c[i] = 0
print(res * 2)
