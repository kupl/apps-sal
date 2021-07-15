p=10**9+7
n=int(input())
a,b,c,d=[input()=="A"for i in range(4)]
if b:b^=1;c^=1;a,d=d^1,a^1
if n<4or not d:print(1)
elif c:print(pow(2,n-3,p))
else:
 l=[1,1]
 for i in range(n):l.append((l[-1]+l[-2])%p)
 print(l[n-2]) 
