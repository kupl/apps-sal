n,b=list(map(int,input().split()))
x=list(map(int,input().split()))
y=list(map(int,input().split()))
s=0
for i in range(b):
    s+=min([abs(x[i]-n),abs(x[i]-1)])+min([abs(y[i]-n),abs(y[i]-1)])
print(s)
    

