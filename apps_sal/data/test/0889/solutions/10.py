lis=[0,0,0,0]
for i in range(4):
    lis[i]=input().strip()

def ch(a,b,c,d):
    return(int(bool(a==b==c or b==c==d or c==d==a or a==b==d)))

check=0
for i in range(3):
    for j in range(3):
       if ch(lis[i][j],lis[i][j+1],lis[i+1][j],lis[i+1][j+1])==1:
           check=1
if check==0:
    print('NO')
else:
    print('YES')

