n = int(input())
t = [[0 for i in range(26)] for j in range(26)]
for i in range(n):
    s = input()
    g = [0 for j in range(26)]
    for j in s:
        g[ord(j) - ord('a')] += 1
    nb = 0
    for j in g:
        if j > 0:
            nb += 1
    if nb == 1:
        l = 0
        for j in range(26):
            if g[j] > 0:
                l = j
        for j in range(26):
            if l != j:
                t[l][j] += len(s)
                t[j][l] += len(s)
    elif nb == 2:
        l1 = -1
        l2 = -1
        for j in range(26):
            if g[j] > 0:
                if l1 == -1:
                    l1 = j
                else:
                    l2 = j
        t[l1][l2] += len(s)
        t[l2][l1] += len(s)
nb = 0
for i in range(26):
    for j in range(26):
        nb = max(t[i][j], nb)
print(nb)
