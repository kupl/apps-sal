n=0
k=0
mat=[]
def check(i,j):
    #print i,j,n,k
    ver_count=1
    hor_count=1
    dial1_count=1
    dial2_count=1
    
    ti=i-1
    tj=j
    #vertical up
    while ti>=0 and mat[ti][j]=='X':
        #print ti,ti,' is X'
        ver_count+=1
        ti-=1
    #print ver_count
    ti=i+1
    #vertical down
    while ti<n and mat[ti][j]=='X':
        #print ti,ti,' is X'
        ver_count+=1
        ti+=1
    #print ver_count
    ti=i
    tj=j-1
    #horizontal left
    while tj>=0 and mat[i][tj]=='X':
        #print ti,ti,' is X'
        hor_count+=1
        tj-=1
    #print hor_count
    tj=j+1
    #horizontal right
    while tj<n and mat[i][tj]=='X':
        #print ti,ti,' is X'
        hor_count+=1
        tj+=1
    #print hor_count
    ti=i-1
    tj=j-1
    #dialonal 1 up left
    while ti>=0 and tj>=0 and mat[ti][tj]=='X':
        #print ti,ti,' is X'
        dial1_count+=1
        ti-=1
        tj-=1
    ti=i+1
    tj=j+1
    #print dial1_count
    #dialonal 1 down right
    while ti<n and tj<n and mat[ti][tj]=='X':
        #print ti,ti,' is X'
        dial1_count+=1
        ti+=1
        tj+=1
    ti=i-1
    tj=j+1
    #print dial1_count
    #diagonal2 up right
    while ti>=0 and tj<n and mat[ti][tj]=='X':
        #print ti,ti,' is X'
        dial2_count+=1
        ti-=1
        tj+=1
    ti=i+1
    tj=j-1
    #print dial2_count
    #diagonal 2 down left
    while ti<n and tj>=0 and mat[ti][tj]=='X':
        #print ti,ti,' is X'
        dial2_count+=1
        ti+=1
        tj-=1
    #print dial2_count
    if ver_count>=k or hor_count>=k or dial1_count>=k or dial2_count>=k:
        return True
    else:
        return False
        
t=eval(input())
while t>0:
    n,k=list(map(int,input().split()))
    tn=n
    mat=[]
    while tn>0:
        mat.append(input().strip())
        tn-=1
    canWin=False
    i=0
    for row in mat:
        j=0
        for cell in row:
            if cell=='.' and check(i,j):
                canWin=True
                break
            j+=1
        i+=1
    if canWin:
        print('YES')
    else:
        print('NO')
    t-=1
