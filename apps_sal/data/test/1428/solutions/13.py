n,c = map(int, input().split())

dl = [list(map(int, input().split())) for _ in range(c)]
nl = [list(map(int, input().split())) for _ in range(n)]

ax = [[0 for i in range(c)] for j in range(3)]

for i in range(n):
    for j in range(n):
        x = (i+j) % 3
        ax[x][nl[i][j]-1] += 1

l = list(range(0,c))
import itertools
ll = list(itertools.permutations(l, 3))
res = float('inf')

#axを変換していくコストを全列挙
for i in ll:
    temp= 0
    for j in range(c):
        temp += ax[0][j]*dl[j][i[0]]
        temp += ax[1][j]*dl[j][i[1]]
        temp += ax[2][j]*dl[j][i[2]]
    res= min(res,temp)
print(res)
