N=int(input())
d=[int(s) for s in input().split()]
x=1
for i in range(N):
    x=x*d[i]
y=0
for i in range(N):
    y+=int(x/d[i])
print(x/y)
