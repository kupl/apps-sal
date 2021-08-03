n, d = list(map(int, input().split()))
s = input()
t = [[-1 for i in range(n + 1)] for j in range(n + 1)]
for i in range(1, n + 1):
    for j in range(i, n + 1):
        if j == i:
            t[i][j] = 1
        else:
            t[i][j] = 0
jes = [0] * 300
for i in range(1, n + 1):
    jes[ord(s[i - 1])] = 1
    t[i][1] = sum(jes)
for j in range(2, n + 1):
    ind = [-1] * 300
    ind[ord(s[j - 1])] = j - 1
    # obliczamy t[j + 1][j], t[j + 2][j], ...
    for i in range(j + 1, n + 1):
        if ind[ord(s[i - 1])] == -1:
            t[i][j] = t[i - 1][j] + t[i - 1][j - 1]
        else:
            t[i][j] = t[i - 1][j] + t[i - 1][j - 1] - t[ind[ord(s[i - 1])]][j - 1]
        ind[ord(s[i - 1])] = i - 1
#t[n][1], t[n][2], ..., t[n][n]
rozne = [t[n][i] for i in range(1, n + 1)]
rozne.reverse()
roz = rozne + [1]
dupa = 0
wyn = 0
for i in range(n + 1):
    if dupa < d:
        k = min(roz[i], (d - dupa))
        dupa += k
        wyn += k * i
    else:
        break
if dupa >= d:
    print(wyn)
else:
    print(-1)
