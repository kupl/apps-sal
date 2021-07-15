X,N=map(int,input().split())
p=sorted(list(map(int,input().split())))

sa_min=100

"""
sa=[]
for i in range(N):
    sa.append(p[i]-X)
"""

for i in range(102):
    if sa_min>abs(i-X) and (not i in p):
        sa_min=abs(i-X)
        ans=i

if N==0:ans=X

print(ans)
