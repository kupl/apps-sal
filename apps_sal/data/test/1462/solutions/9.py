temp = input().split()
(N, K) = (int(temp[0]), int(temp[1]))
s = input()
d = dict()
for c in s:
    d[c] = d.get(c, 0) + 1
sum = 0
while K > 0:
    m = '-'
    for (k, v) in list(d.items()):
        if d.get(m, 0) < v:
            m = k
    if K > d[m]:
        sum += d[m] * d[m]
        K -= d[m]
    else:
        sum += K * K
        K = 0
    d[m] = 0
print(sum)
