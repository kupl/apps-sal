n = int(input())
rs = []
cs = [0 for i in range(n)]
d1 = 0
d2 = 0
for i in range(n):
    ip = list(map(int, input().split()))
    rs.append(sum(ip))
    if 0 in ip:
        l = i
        k = ip.index(0)
    for j in range(n):
        cs[j] += ip[j]
    d1 += ip[i]
    d2 += ip[n - i - 1]
if n == 1:
    print(1)
else:
    if l == 0:
        r = rs[1]
    else:
        r = rs[0]
    ans = r - rs[l]
    if l == k:
        d1 += ans
    if l == n - k - 1:
        d2 += ans
    rc = 0
    cc = 0
    for i in rs:
        if i != r:
            rc += 1
    for i in cs:
        if i != r:
            cc += 1
    if rc != 1 or cc != 1:
        print(-1)
    elif d1 != r or d2 != r:
        print(-1)
    elif ans <= 0:
        print(-1)
    else:
        print(ans)
