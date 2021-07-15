n = int(input())
g = []
r = [0]*n
c = [0]*n
for i in range(n):
    g.append(list(input()))
    x = [a for a in range(n) if g[i][a] == '.']
    if len(x) > 0: r[i] = 1
    for j in x: c[j] = 1
if sum(r) == n:
    for i in range(n):
        for j in range(n):
            if g[i][j] == '.':
                print('%i %i' % (i+1,j+1))
                break
elif sum(c) == n:
    for i in range(n):
        for j in range(n):
            if g[j][i] == '.':
                print('%i %i' % (j+1,i+1))
                break
else:
    print(-1)
