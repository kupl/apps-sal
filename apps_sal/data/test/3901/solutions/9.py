from fractions import gcd
n = int(input())
a = [int(z) for z in input().split()]
cnt = 0
for i in range(n):
    if a[i] == 1:
        cnt += 1
if cnt > 0:
    print(n - cnt)
    return
minlen = 1000000000
for l in range(n):
    cur = a[l]
    for r in range(l + 1, n):
        cur = gcd(cur, a[r])
        if cur == 1:
            minlen = min(minlen, r - l)
            
if minlen == 1000000000:
    print(-1)
else:
    print(minlen + n - 1)
