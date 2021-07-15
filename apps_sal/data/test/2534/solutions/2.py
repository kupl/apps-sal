r,c=map(int,input().split())
mat=[]
l=[]
flag=0
for i in range(r):
    t_1=list(map(int,input().split()))
    l.append(min(t_1))
    mat.append(t_1)
r_1=[]
for i in range(c):
    x=[]
    for j in range(r):
        x.append(mat[j][i])
    r_1.append(max(x))
for i in l:
    if i in r_1:
        print(i)
        flag=1
        break
if flag==0:
    print('GUESS')

