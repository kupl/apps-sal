import numpy as np
n,t=map(int,input().split())
a=[list(map(int,input().split()))for i in range(n)]
b=np.zeros((n+1,t))
c=np.zeros((n+1,t))
for i in range(n):
    b[i+1]=b[i]
    b[i+1][a[i][0]:]=np.maximum(b[i+1][a[i][0]:],b[i][:-a[i][0]]+a[i][1])
    c[-i-2]=c[-i-1]
    c[-i-2][a[-i-1][0]:]=np.maximum(c[-i-2][a[-i-1][0]:],c[-i-1][:-a[-i-1][0]]+a[-i-1][1])
q=0
for i in range(n):
    q=max(q,max(b[i]+c[i+1][::-1])+a[i][1])
print(int(q))
