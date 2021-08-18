
h, w, k = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(h)]

ret = 100000
for i in range(2 ** (h - 1)):
    hi = [0] * h
    for j in range(h - 1):
        hi[j + 1] += hi[j] + (i >> j & 1)
    cnt = max(hi)
    pj = 0
    x = []
    while pj < w:
        s = [0] * 10
        fg = False
        for j in range(pj, w):
            for t in range(h):
                s[hi[t]] += a[t][j]
            if max(s) > k:
                if j == pj:
                    cnt = 100000
                    fg = True
                    break
                else:
                    x.append(j)
                    cnt += 1
                    pj = j
                break
            if j == w - 1:
                pj = w
                break
        if fg:
            break
    ret = min(ret, cnt)
print(ret)
