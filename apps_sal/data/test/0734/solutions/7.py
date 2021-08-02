from collections import Counter as C
n, m = map(int, input().split())
l = [*map(int, input().split())]
c = sorted(C(l).items())

res = 0
j = 0
for hi, ni in c:
    # print(hi, ni, j)
    h = min(hi - j, ni) + j
    res += (hi - 1) * ni
    if h > j:
        j = h
m = max(l)
if j < m:
    res -= m - j
print(res)
