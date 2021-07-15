n = int(input())
l = [*map(int, input().split())]

e_pre, o_pre = [0], [0]
for i, e in enumerate(l):
    if i & 1:
        e_pre.append(e_pre[-1] + e)
        o_pre.append(o_pre[-1])
    else:
        o_pre.append(o_pre[-1] + e)
        e_pre.append(e_pre[-1])

o_pre.append(o_pre[-1])
e_pre.append(e_pre[-1])


res = 0

for i, ele in enumerate(l):
    e = e_pre[i] + (o_pre[-1] - o_pre[i + 1])
    o = o_pre[i] + (e_pre[-1] - e_pre[i + 1])
    if e == o:
        res += 1
print(res)
