n, m = map(int, input().split())
A = ['#'*(m+2)]
for i in range(1, n+1):
    B = ['#'] + list(input()) + ['#']
    A.append(B)
    if 'S' in B:
        C = [i, B.index('S')]
A.append('#'*(m+2))
N = C.copy()
q = 'L'
sh = 0
while sh==0 or N!=C:
    sh+=1
    if (A[N[0]-1][N[1]]=='*' or A[N[0]-1][N[1]]=='S') and q!='D':
        N[0]-=1
        print('U', end='')
        q = 'U'
    elif (A[N[0]+1][N[1]]=='*' or A[N[0]+1][N[1]]=='S') and q!='U':
        N[0]+=1
        print('D', end='')
        q = 'D'   
    elif (A[N[0]][N[1]-1]=='*' or A[N[0]][N[1]-1]=='S') and q!='R':
        N[1]-=1
        print('L', end='')
        q = 'L'  
    elif (A[N[0]][N[1]+1]=='*' or A[N[0]][N[1]+1]=='S') and q!='L':
        N[1]+=1
        print('R', end='')
        q = 'R'    
