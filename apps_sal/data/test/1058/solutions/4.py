def min(a, b):
    if a < b:
        return a
    return b
def max(a,b):
    return abs(min(-a,-b))
been = [0 for i in range(4)]
ans = 0
minw = 10**18
degpar = [0 for i in range(4)]
w = [0 for i in range(4)]
gr = [list() for i in range(4)]
rem = [[0 for i in range(4)] for j in range(4)]
def dfs(x, l):
    l.append(w[x])
    if been[x]:
        return
    been[x] = 1
    for i in gr[x]:
        if been[i] == 0 and rem[x][i] > 0:
            dfs(i, l)
n = int(input())
blocks = []
for i in range(n):
    a,v,b = list(map(int, input().split()))
    a -= 1
    b -= 1
    if a != b:
        blocks.append([a,v,b])
    w[b] += v
    if a != b:
        minw = min(minw, v)
    degpar[a] += 1
    degpar[a] %= 2
    degpar[b] += 1
    degpar[b] %= 2
    gr[a].append(b)
    gr[b].append(a)
    rem[a][b] += 1
    rem[b][a] += 1
ok = True
for i in range(4):
    l = []
    if been[i] == 0:
        dfs(i, l)
    if i == 0 and all(been) and all(degpar):
        ok = False
        break
    ans = max(ans, sum(l))
if ok:
    print(ans)
    return
for p in blocks:
    i = p[0]
    j = p[2]
    w[j] -= p[1]
    been = [0 for i in range(4)]
    rem[i][j] -= 1
    rem[j][i] -= 1
    #print(i)
    #print(j)
    #print(':')
    for x in range(4):
        l = []
        if been[x] == 0:
            dfs(x,l)
        ans = max(ans, sum(l))
        #print(sum(l))
    w[j] += p[1]
    rem[i][j] += 1
    rem[j][i] += 1
print(ans)

