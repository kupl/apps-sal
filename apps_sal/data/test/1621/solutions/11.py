s=input()
k=int(input())
A=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
c=list(map(int,input().split()))
l=len(s)
u=max(c)
cost=0
for i in range (len(s)):
	cost=cost+(i+1)*c[A.index(s[i])]
for i in range(k):
	cost=cost+(l+i+1)*u
print(cost)
