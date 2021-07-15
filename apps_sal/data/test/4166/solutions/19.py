n, m = map(int, input().split())
N = [0]*n
t = [0]*n
if n>1:
    N[0]=1
f = 0
for i in range(m):
    s, c = map(int, input().split())
    if t[s-1]!=0 and N[s-1]!=c:
        f = 1
    t[s-1] = 1
    N[s-1] = c

if n!=1 and N[0]==0:
    print(-1)

elif f==1:
    print(-1)

else:
    for i in range(n):
        print(N[i],end="")
