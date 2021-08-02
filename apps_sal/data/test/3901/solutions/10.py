import math
n = int(input())
l = list(map(int, input().split()))

if l.count(1): print(n - l.count(1))
else:
    tmp1 = n + 1
    for i in range(n):
        tmp2 = l[i]
        for j in range(n - i):
            tmp2 = math.gcd(tmp2, l[i + j])
            if (tmp2 == 1): tmp1 = min(tmp1, j)
    if (tmp1 == n + 1): print("-1")
    else: print(tmp1 + n - 1)
