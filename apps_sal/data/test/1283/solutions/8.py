n, k = list(map(int, input().split(" ")))

rows = []
for i in range(n):
    rows +=  [ input() ] 

cnt = [[0 for i in range(n) ] for j in range(n)]

for i in range(n):
    for j in range(n):
        flag = True
        for kk in range(k):
            if j + kk > n - 1 or  rows[i][j + kk] == '#':
                flag = False
                break
        if flag:
            for kk in range(k):
                cnt[i][j + kk] += 1
        flag = True
        for kk in range(k):
            if i + kk > n - 1 or rows[i + kk][j] == '#':
                flag = False
                break
        if flag:
            for kk in range(k):
                cnt[i + kk][j] += 1
         
mx = 0
ia = 0
ij = 0
for i in range(n):
    for j in range(n):
        if cnt[i][j] > mx:
            mx = cnt[i][j]
            ia = i
            ij = j

print(ia + 1, ij + 1)

