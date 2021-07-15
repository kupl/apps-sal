n, q = list(map(int, input().split()))
C = [0 for _ in range(n)]
X = [[-1, -1] for _ in range(n)]
ii = 1
for i in range(q):
    l, r = list(map(int, input().split()))
    ii += 1
    l -= 1
    r -= 1
    for j in range(l, r+1):
        if C[j] <= 2:
            C[j] += 1
            if C[j] <= 2:
                X[j][C[j]-1] = i
s = len([c for c in C if c > 0])

ma = 0
for i in range(q):
    Y = [0] * q
    Y[i] = 10**10
    y = 0
    for j in range(n):
        if C[j] == 2:
            if i == X[j][0] or i == X[j][1]:
                Y[X[j][0]] += 1
                Y[X[j][1]] += 1
        elif C[j] == 1:
            if i == X[j][0]:
                y += 1
            else:
                Y[X[j][0]] += 1
            
    ma = max(ma, s-min(Y)-y)

print(ma)

