N,M=list(map(int,input().split()))
def f(n):
   return n*(n-1)//2
ans=f(N)
root=[i for i in range(N+1)]
height=[1]*(N+1)
def find(a):
   f=a
   if a==root[a]:
      return a
   while a!=root[a]:
      a=root[a]
   root[f]=a
   return a
def union(a,b):
   A=find(a)
   B=find(b)
   nonlocal ans
   if A==B:
      return
   ans+=f(height[A])+f(height[B])
   if height[A]>height[B]:
      root[B]=root[A]
      height[A]+=height[B]
      height[B]=0
   else:
      root[A]=root[B]
      height[B]+=height[A]
      height[A]=0
   ans-=f(max(height[A],height[B]))
l=[tuple(map(int,input().split())) for i in range(M)]
l=l[::-1]
ans_m=[ans]
for i in range(M):
   a,b=l[i]
   union(a,b)
   ans_m.append(ans)
ans_m=ans_m[::-1]
for i in range(1,M+1):
   print(ans_m[i])
