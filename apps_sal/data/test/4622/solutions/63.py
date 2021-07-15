n=int(input())
a=list(map(int,input().split()))
m=len(a)
a=set(a)
n=len(a)
if m==n:
  print("YES")
else:
  print("NO")
