(n, m) = [int(x) for x in input().split()]
a = []
for i in range(n):
    a.append(input())
res = 0
z = ['face', 'faec', 'feac', 'feca', 'fcae', 'fcea', 'eafc', 'eacf', 'ecaf', 'ecfa', 'efac', 'efca', 'acfe', 'acef', 'aecf', 'aefc', 'afce', 'afec', 'cafe', 'caef', 'ceaf', 'cefa', 'cfea', 'cfae']
for i in range(1, n):
    for j in range(1, m):
        if a[i][j] + a[i][j - 1] + a[i - 1][j] + a[i - 1][j - 1] in z:
            res += 1
print(res)
