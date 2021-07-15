N, C = map(int, input().split())

D = []
for i in range(C):
    D.append(list(map(int, input().split())))

cc = [[0]*C for i in range(3)]
for i in range(N):
    color = list(map(int, input().split()))
    for j in range(len(color)):
        cc[(i+j)%3][color[j]-1] += 1
    
iwakan = [[[0, 0] for _ in range(C)] for _ in range(3)]

for i in range(3):
    for j in range(C):
        tmp = 0
        for k in range(len(cc[i])):
            tmp += cc[i][k]*D[k][j]
        iwakan[i][j][0] = tmp
        iwakan[i][j][1] = j

ans = 10**15
for i in range(len(iwakan)):
    iwakan[i] = sorted(iwakan[i], key=lambda x:x[0])
    
for i in range(3):
    for j in range(3):
        if(iwakan[0][i][1] == iwakan[1][j][1]):
            continue
        for k in range(3):
            if(iwakan[0][i][1] == iwakan[2][k][1]):
                continue
            if(iwakan[1][j][1] == iwakan[2][k][1]):
                continue
            ans = min(ans, iwakan[0][i][0]+iwakan[1][j][0]+iwakan[2][k][0])
            
print(ans)
