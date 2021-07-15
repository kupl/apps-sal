a,b=map(int,input().split())
c=input().split()
c=[int(i) for i in c]
x=0
c.sort()
for i in range(b):
    x+=c[len(c)-i-1]
print(x)
