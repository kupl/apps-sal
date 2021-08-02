import numpy as np

n, c = list(map(int, input().split()))
stc = [[] for i in range(c + 1)]
for i in range(n):
    s_, t_, c_ = list(map(int, input().split()))
    stc[c_].append([s_, t_])


stc_ = []
for i in range(1, c + 1):
    stc[i] = sorted(stc[i], key=lambda x: (x[0], x[1]))
    j = 0
    l = len(stc[i])
    flg = False
    while j < l:
        if not flg:
            cs, ct = stc[i][j][0], stc[i][j][1]
        if j == l - 1:
            stc_.append([cs, ct])
            break
        ns, nt = stc[i][j + 1][0], stc[i][j + 1][1]
        if ct != ns:
            flg = False
            stc_.append([cs, ct])
        else:
            flg = True
            ct = nt
            if j == l - 2:
                stc_.append([cs, ct])
                break
        j += 1
stc_ = sorted(stc_, key=lambda x: (x[0], x[1]))

m = len(stc_)

cnt = np.zeros(10**5 + 5, dtype=int)
for i in range(m):
    s, t = stc_[i][0] - 1, stc_[i][1]
    cnt[s:t] += 1
print((cnt.max()))
