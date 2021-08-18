n, m = [int(i) for i in input().split()]
nl = [int(i) for i in input().split()]
ml = []
for i in range(m):
    t, r = [int(k) for k in input().split()]
    ml.append((t, r))

mll = [(0, 0)]
for i in range(m - 1, -1, -1):
    if i == m - 1:
        mll.append(ml[i])
    elif i != m - 1 and ml[i][1] > mll[-1][1]:
        mll.append(ml[i])


temp = sorted(nl[:mll[len(mll) - 1][1]])
x, y = 0, len(temp) - 1
for i in range(len(mll) - 1, 0, -1):
    t, r = mll[i]
    for j in range(r - 1, mll[i - 1][1] - 1, -1):
        if t == 1:
            nl[j] = temp[y]
            y -= 1
        elif t == 2:
            nl[j] = temp[x]
            x += 1

for i in range(n):
    nl[i] = str(nl[i])
print(' '.join(nl))
