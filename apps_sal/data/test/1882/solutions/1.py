n, t = list(map(int, input().split()))
ts = []
for i in range(n):
    a, c = list(map(int, input().split()))
    ts.append((a, c, i))
ts = sorted(ts, key=lambda x: x[1])
ans = 0
ptr = 0
hc = {}
hs = {}
csize = 0
ctime = 0
for i in range(n):
    n_ans = ans + 1
    if n_ans - 1 in hc:
        csize -= hc[n_ans - 1]
        ctime -= hs[n_ans - 1]
    fail = False
    while csize < n_ans:
        if ptr == n:
            fail = True
            break
        a, c, num = ts[ptr]
        if a >= n_ans:
            csize += 1
            ctime += c
            if a not in hc:
                hc[a] = 0
            hc[a] += 1
            if a not in hs:
                hs[a] = 0
            hs[a] += c

        ptr += 1
        if ctime > t:
            fail = True
            break
    if fail:
        break
    else:
        ans = n_ans

print(ans)
print(ans)
tks = []
for i in range(ptr):
    if len(tks) == ans:
        break
    if ts[i][0] >= ans:
        tks.append(ts[i][2])

print(' '.join([str(i + 1) for i in tks]))
