import bisect
a = []
a.append(0)
tsl = 0
wsl = 0
upto = 1000008
for i in range(1, upto):
    numl = len(str(i))
    tsl += numl
    wsl += tsl
    a.append(wsl)
ss = [0]
for i in range(1, upto):
    for j in str(i):
        ss.append(j)
q = int(input())
for i in range(q):
    k = int(input())
    now = bisect.bisect_left(a, k)
    k -= a[now - 1]
    print(ss[k])
