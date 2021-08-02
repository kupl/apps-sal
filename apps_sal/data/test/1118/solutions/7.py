def lps(str):
    n = len(str)

    L = [[0 for x in range(n)] for x in range(n)]

    for i in range(n):
        L[i][i] = 1

    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if str[i] == str[j] and cl == 2:
                L[i][j] = 2
            elif str[i] == str[j]:
                L[i][j] = L[i + 1][j - 1] + 2
            else:
                L[i][j] = max(L[i][j - 1], L[i + 1][j])

    return L[0][n - 1]


n = input()
n = int(n)
l = list(map(str, input().strip().split()))
seq = [l[0]]
ch = l[0]
for i in range(1, n):
    if l[i] != ch:
        ch = l[i]
        seq.append(l[i])
n = len(seq)
print(n - lps(seq) // 2 - 1)
