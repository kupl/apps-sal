
def f(t, x):
    for i in range(1, len(t) + 1):
        ps[i] = ps[i - 1] + t[i - 1][0] * t[i - 1][1]
    l = 0
    r = len(t) + 1
    while l < r:
        s = (l + r) // 2
        if ps[s] <= x:
            l = s + 1
        else:
            r = s
    return l - 1

n , T = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
t = [(int(x) - T,  a[i]) for i, x in enumerate(input().split())]

tp = list(sorted([e for e in t if e[0] > 0]))
tm = list(sorted([(-x[0], x[1]) for x in ([e for e in t if e[0] < 0])]))
ep = sum(e[0] * e[1] for e in tp)
em = sum(e[0] * e[1] for e in tm)
ps = [0] * (n + 1)
res = sum([e[1] for e in [e for e in t if e[0] == 0]])
if ep > 0 and em > 0:
    if ep < em:
        it = f(tm, ep)

        res += sum([e[1] for e in tp])
        res += sum([e[1] for e in tm[:it]])
        if  it < len(tm):
            res += (ep - ps[it]) / tm[it][0]
    else:
        it = f(tp, em)
        res += sum([e[1] for e in tm])
        res += sum([e[1] for e in tp[:it]])
        if  it < len(tp):
            res += (em - ps[it]) / tp[it][0]
print(res)


