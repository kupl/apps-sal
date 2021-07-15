N=int(input())
t=[0]
x=[0]
y=[0]
for _ in range(N):
    a,b,c=list(map(int,input().split()))
    t.append(a)
    x.append(b)
    y.append(c)

for i in range(N):
    X=abs(x[i+1]-x[i])+abs(y[i+1]-y[i])
    T=abs(t[i+1]-t[i])
    if X>T or X%2!=T%2:
        print("No")
        break
else:
    print("Yes")

