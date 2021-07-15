M = 10**9 + 7
R = lambda: map(int, input().split())
n = int(input())
for i in range(n):
    n,m = R()
    L = [[0 for i in range(m)] for j in range(n)]
    a = []
    for i in range(n):
        a.append(input())
    for i in range(n):
        c = 0
        for j in range(m):
            if a[i][j] == '.':c += 1
        for j in range(m):
            L[i][j] = c
    for i in range(m):
        c = 0
        for j in range(n):
            if a[j][i] == '.':c += 1
        for j in range(n):
            L[j][i] += c
    mi = 10**9
    k = []
    for i in range(n):
        for j in range(m):
            mi = min(mi,L[i][j])
    for i in range(n):
        for j in range(m):
            if L[i][j] == mi and a[i][j] == '.':
                mi -= 1
    print(mi)
