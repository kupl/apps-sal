import sys
H, W = list(map(int, input().split()))
l = []

for i in range(H):
    l.append(list(input()))

for i in range(H):
    for j in range(W):
        
        if l[i][j] == '.':
            pass
        else:
            count = 0
            if i > 0 and l[i-1][j] == '#':
                    count += 1 #上方向
            if i < (H-1) and l[i+1][j] == '#':
                count += 1     #下方向
            if j > 0 and l[i][j-1] == '#':
                count += 1     #左方向
            if j < (W-1) and l[i][j+1] == '#':
                count += 1     #右方向
            if count == 0:
                print('No')
                return
                
print('Yes')

