n = int(input())
A = [int(x) for x in input().split()]

from collections import defaultdict as dd


hsh = dd(int)
for i in range(n):
    hsh[A[i]] += 1

cnt = 0
ans = 10000000

for i in hsh:
    if hsh[i] >= 2:
        cnt += 1
if len(set(A)) == n:
    print(0)
else:
    for i in range(n):
        hsh2 = dd(int)
        ct = 0
        for j in range(i, n):
            hsh2[A[j]] += 1
            if hsh2[A[j]] == hsh[A[j]] - 1 and hsh[A[j]]  >= 2:
                ct += 1
            if ct == cnt:
                ans = min(ans, abs(j - i + 1))
                
    print(ans)

