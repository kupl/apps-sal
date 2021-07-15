n,k=map(int,input().split())
d=list(map(int,input().split()))
x=list(range(1,100001))
y=[0]*100000
for i in range(100000):
    s=str(i)
    S=len(s)
    for j in range(S):
        if int(s[j]) in d:
            y[i-1]=1
            break
for i in range(100000):
    if i>=n-1:
        if y[i]==0:
            print(i+1)
            break
