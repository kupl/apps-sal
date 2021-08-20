import sys
input = sys.stdin.readline
mod = 1000000007
for f in range(int(input())):
    n = int(input())
    neig = [0] * n
    for i in range(n):
        neig[i] = [0]
    edges = []
    for i in range(n - 1):
        (vertexa, vertexb) = map(int, input().split())
        vertexa -= 1
        vertexb -= 1
        neig[vertexa][0] += 1
        neig[vertexb][0] += 1
        neig[vertexa].append(vertexb)
        neig[vertexb].append(vertexa)
        edges.append([vertexa, vertexb])
    tod = []
    upn = [-1] * n
    dn = [1] * n
    for i in range(n):
        if neig[i][0] == 1:
            tod.append(i)
    while len(tod) > 0:
        x = tod.pop()
        neig[x][0] = 0
        for foo in range(1, len(neig[x])):
            v = neig[x][foo]
            if neig[v][0] > 0:
                neig[v][0] -= 1
                upn[x] = v
                dn[v] += dn[x]
                if neig[v][0] == 1:
                    tod.append(v)
    m = int(input())
    p = list(map(int, input().split()))
    p.sort(reverse=True)
    facs = [1] * (n - 1)
    if m < n:
        for i in range(m):
            facs[i] = p[i]
    else:
        diff = m - (n - 1)
        for j in range(diff):
            facs[0] *= p[j]
            facs[0] %= mod
        for j in range(diff, m):
            facs[j - diff] *= p[j]
    wedgies = [0] * (n - 1)
    for i in range(n - 1):
        (a, b) = (edges[i][0], edges[i][1])
        if upn[a] == b:
            wedgies[i] = dn[a] * (n - dn[a])
        else:
            wedgies[i] = dn[b] * (n - dn[b])
    wedgies.sort(reverse=True)
    sol = 0
    for i in range(n - 1):
        sol += wedgies[i] * facs[i]
        sol %= mod
    print(sol)
