import itertools as it
(n, m) = map(int, input().split())
e = [[0 for i in range(n)] for j in range(n)]
for i in range(m):
    (a, b) = map(lambda x: int(x) - 1, input().split())
    e[a][b] = 1
    e[b][a] = 1
c = 0
for t in it.permutations([j + 1 for j in range(n - 1)]):
    i = (0,) + t
    c += 1
    for j in range(n - 1):
        if e[i[j]][i[j + 1]] == 0:
            c -= 1
            break
print(c)
