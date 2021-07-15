import sys

n,m=list(map(int,input().split()))
l=[[] for i in range(n)]

for i in range(m):
  a,b=list(map(int,input().split()))
  l[a-1].append(b)
# print(l)


for i in l[0]:
  for j in l[i-1]:
    if j==n:
      print("POSSIBLE")
      return

print("IMPOSSIBLE")


