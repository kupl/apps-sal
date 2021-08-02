h, w, k = map(int, input().split(' '))
c = [input() for x in range(h)]
cnt = 0
for m in range(2**(h + w)):
    cc = c.copy()
    for ij in range(h + w):
        if ((m >> ij) & 1):
            if ij in range(h):
                cc[ij] = '.' * w
            if ij in range(h, h + w):
                for t in range(h):
                    cc[t] = cc[t][:ij - h] + '.' + cc[t][ij + 1 - h:]
    num = sum(cc[s].count('#') for s in range(h))
    if num == k:
        cnt += 1
print(cnt)
