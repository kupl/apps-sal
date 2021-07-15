def dg(m, i0, j0, d):
    return [m[(i0 + i - 1)%len(m)][(j0 + d*i - 1)%len(m[0])] for i in range(len(m))]

def column(matrix, i):
    return [row[i] for row in matrix]

import re
for _ in range(eval(input())):
    n,k = list(map(int,input().split()))
    f=0
    st = 'X'*k
    a=[]
    for j in range(n):
        l = input()
        a.append(list(l))
    fd = [[a[y-x][x] for x in range(n) if 0<=y-x<n] for y in range(2*n-1)]
    s=list(reversed(list(zip(*a))))
    bd = [[s[y-x][x] for x in range(n) if 0<=y-x<n] for y in range(2*n-1)]
    for i in range(n):
        for j in range(n):
            if a[i][j]=='.' and f==0:
                a[i][j]='X'
                if len(re.findall(st,''.join(a[i])))!=0:
                    f=1
                    print("YES")
                    break
                elif len(re.findall(st,''.join(column(a,j))))!=0:
                    f=1
                    print("YES")
                    break
                a[i][j]='.'
    if f==0:
        for i in range(len(fd)):
            for j in range(len(fd[i])):
                if fd[i][j]=='.' and f==0:
                    fd[i][j]='X'
                    if len(re.findall(st,''.join(fd[i])))!=0:
                        f=1
                        print("YES")
                        break
                    fd[i][j]='.'
                if bd[i][j]=='.' and f==0:
                    bd[i][j]='X'
                    if len(re.findall(st,''.join(bd[i])))!=0:
                        f=1
                        print("YES")
                        break
                    bd[i][j]='.'
    if f==0:
        print("NO")
