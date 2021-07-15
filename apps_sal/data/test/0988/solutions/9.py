cc = [[3,3,0,4,4,0,3,3],[3,3,0,4,4,0,3,3], [2,2,0,3,3,0,2,2] , [2,2,0,3,3,0,2,2],[1,1,0,2,2, 0,1,1],[1,1,0,2,2,0,1,1]]
m = 0
mi = -1
mj = -1
ss=[]
for i in range(6):
    s = list(input())
    ss.append(s)
    for j in range(8):
        if s[j] == '.':
            if cc[i][j] > m:
                m = cc[i][j]
                mi = i
                mj = j
if mi != -1 and mj != -1:
    ss[mi][mj] = 'P'
for i in range(6):
    print(''.join(ss[i]))
