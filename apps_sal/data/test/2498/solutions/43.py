import math
(n, m) = list(map(int, input().split()))
al = list(map(int, input().split()))
twos = set()
for c in al:
    (temp, tempc) = (0, c)
    while tempc % 2 == 0:
        tempc //= 2
        temp += 1
    twos.add(temp)
if len(twos) > 1:
    print(0)
else:
    lcmv = al[0]
    for i in range(1, n):
        lcmv = lcmv * al[i] // math.gcd(lcmv, al[i])
    print(max(0, 1 + (m - lcmv // 2) // lcmv))
