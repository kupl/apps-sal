Blue=[]
Red=[]

n=int(input())
for i in range(n):
    s=input()
    Blue.append(s)
    
m=int(input())
for i in range(m):
    t=input()
    Red.append(t)

ans=0
for a in Blue:
    plus = Blue.count(a)
    minus = Red.count(a)
    point = plus - minus
    ans = max(ans, point)
print(ans)
