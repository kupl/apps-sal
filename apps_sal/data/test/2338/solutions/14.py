n=int(input())
d=[]
for i in range(n):
    x,y=list(map(int,input().split()))
    d.append([(x**2+y**2)**(0.5),x,y])
d.sort()
ans=[]
for i in range(n):
    if d[i][1]<0:
        ans.append('1 '+str(-d[i][1])+' L')
    elif d[i][1]>0:
        ans.append('1 '+str(d[i][1])+' R')
    if d[i][2]<0:
        ans.append('1 '+str(-d[i][2])+' D')
    elif d[i][2]>0:
        ans.append('1 '+str(d[i][2])+' U')
    ans.append('2')
    if d[i][2]<0:
        ans.append('1 '+str(abs(d[i][2]))+' U')
    elif d[i][2]>0:
        ans.append('1 '+str(abs(d[i][2]))+' D')
    if d[i][1]<0:
        ans.append('1 '+str(abs(d[i][1]))+' R')
    elif d[i][1]>0:
        ans.append('1 '+str(abs(d[i][1]))+' L')
    ans.append('3')
print(len(ans))
print('\n'.join(ans))
