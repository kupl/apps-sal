from math import ceil

n = int(input())
cs = []
ss = []
fs = []

for _ in range(n-1):
    c, s, f = map(int, input().split())
    cs.append(c)
    ss.append(s)
    fs.append(f)

for i in range(n):
    t = 0
    for j in range(i, n-1):
        if t < ss[j]:
            t = ss[j]
        t = ceil(t / fs[j]) * fs[j]
        t += cs[j]
    print(t)
