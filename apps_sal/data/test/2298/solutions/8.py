from math import gcd

t = int(input())
for __ in range(t):
    a,b,q = list(map(int,input().split()))
    if a > b:
        a, b = b, a
    g = a * b // gcd(a, b)

    # 1以上m以下
    def solve(m):
        if m == 0:
            return 1
        aa,bb = divmod(m + 1, g)
        ret = aa * b
        ret += min(bb, b)
        return ret
    
    def br(l, r):
        ret = 0
        for i in range(l, r + 1):
            if (i % a) % b != (i % b) % a:
                ret += 1
        return ret

    res = []
    # brt = []
    for _ in range(q):
        l,r = list(map(int,input().split()))
        if b % a == 0:
            res.append(0)
        else:
            res.append(r - l + 1 - (solve(r) - solve(l - 1)))
        # brt.append(br(l, r))
    print(*res)
    # print(*brt)

