from collections import defaultdict
from math import sqrt, factorial, gcd, log2, inf, ceil
mod = 10**9 + 7


q = int(input())

for _ in range(q):
    n, k = list(map(int, input().split()))
    s = list(input())
    cnt = 0
    flag = 0
    yo = 0
    ha = 0
    for i in range(n):

        if s[i] == '0':
            if cnt <= k:
                k -= cnt
                yo += 1
            else:
                flag = 1
                ha = k
                break
        else:
            cnt += 1
    if flag == 0:
        z = list(map(int, s))
        z.sort()
        z = list(map(str, z))
        print(''.join(z))

    else:
        ans = []
        for i in range(yo):
            ans.append('0')
        cnt = 0
        ma = 0

        for j, i in enumerate(s):
            if i == '1':
                ma += 1
            if i == '0':
                cnt += 1
            if cnt > yo:
                posn = j
                break
        z = ['1' * (ma - ha) + '0'] + ['1' * (ha)]
        z1 = s[posn + 1:]
        ans += z + z1
        print(''.join(ans))
