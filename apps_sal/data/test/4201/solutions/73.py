h, w, k = map(int, input().split())
c = []
black = 0
for _ in range(h):
    tmp = input()
    black += tmp.count('
    c.append(tmp)

cnt=0
for i in range(2**h):
    for j in range(2**w):
        bl=black
        for ii in range(h):
            for jj in range(w):
                if (i & (1 << ii)) or (j & (1 << jj)):
                    if c[ii][jj] == '
                        bl -= 1
        if bl == k:
            cnt += 1
print(cnt)
