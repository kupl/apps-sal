n = int(input())
s = list(map(int, input().split()))
h = max(s)
ss = [0] * (h + 1)
for i in s:
    ss[i] += 1
(f, x) = ([0] * h, 0)
for j in reversed(ss):
    x += j
    f.append(x)
f.reverse()
res = []
for i in range(len(ss)):
    ch = ss[i]
    if ch:
        (summ, x) = (0, f[i])
        for j in range(i, h + 1, i):
            o = f[j + i]
            summ += (x - o) * j
            x = o
        res.append(summ)
print(max(res))
