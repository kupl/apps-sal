l = [list(map(int,input().split())) for i in range(3)]
n = int(input())
b = list(int(input()) for _ in range(n))
for i in range(3) :
    for j in range(3) :
        for k in range(n) :
            if l[i][j] == b[k] :
                l[i][j] = 0

for i in range(3) :
    if l[i][0] + l[i][1] + l[i][2] == 0 :
        print('Yes')
        return
    if l[0][i] + l[1][i] + l[2][i] == 0 :
        print('Yes')
        return
    if l[0][0] + l[1][1] + l[2][2] == 0 :
        print('Yes')
        return
    if  l[0][2] + l[1][1] + l[2][0] == 0 :
        print('Yes')
        return
print('No')
