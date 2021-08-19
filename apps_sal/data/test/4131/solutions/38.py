(N, M) = map(int, input().split())
py = [list(map(int, input().split())) + [i] for i in range(M)]
py.sort()
P = py[0][0]
c = 0
ans = []
for (p, y, i) in py:
    if p == P:
        c += 1
    else:
        P = p
        c = 1
    ansc = str(c)
    ansp = str(p)
    anser = '0' * (6 - len(ansp)) + ansp + '0' * (6 - len(ansc)) + ansc
    ans.append([i, anser])
ans.sort()
for (i, anser) in ans:
    print(anser)
