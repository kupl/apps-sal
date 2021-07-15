n=int(input())
s,t=[],[]
for i in range(n):
    a,b=map(int,input().split())
    s.append(a)
    t.append(b)
s=sorted(s)
t=sorted(t)
if n%2==0:
    print(t[n//2-1]+t[n//2]-s[n//2-1]-s[n//2]+1)
else:
    print(t[n//2]-s[n//2]+1)
