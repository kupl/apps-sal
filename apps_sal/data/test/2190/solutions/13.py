import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

n, k = map(int, input().split())
a = list(map(int, input().split()))


def factors(n, k):
    i = 2
    sq = int(n**0.5) + 1
    di = {}
    while n != 1:
        if n % i == 0:
            cur = 0
            while n % i == 0:
                n = n // i
                cur += 1
            if cur % k != 0:
                di[i] = cur % k
        i += 1
        if i > sq: break
    if n != 1:
        di[n] = 1
    return "|".join("%d:%d" % (i, di[i]) for i in di)


ft = {}
di = {}

for i in a:
    ft[i] = factors(i, k)
    di[ft[i]] = 1 if ft[i] not in di else di[ft[i]] + 1

ans = 0
for i in a:
    ftt = ft[i]
    if ftt == "":
        ans += di[ftt] - 1
    else:
        dx = {}
        for oo in ftt.split("|"):
            x, y = map(int, oo.split(":"))
            dx[x] = - y % k
        ftt2 = "|".join("%d:%d" % (i, dx[i]) for i in dx)
        if ftt == ftt2:
            ans += di[ftt2] - 1
        else:
            if ftt2 in di:
                ans += di[ftt2]

print(ans // 2)
