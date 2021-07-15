import sys
input=sys.stdin.readline # for speed up

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
diff=[0]*n
for ii in range(n):
  diff[ii]=b[ii]-a[ii]

# union find
parent=list(range(n))
rank=[0]*n

def findroot(x):
  if parent[x]!=x:
    parent[x]=findroot(parent[x])
  return parent[x]

def unite(x,y):
  x = findroot(x)
  y = findroot(y)
  if x != y: # not a same group
    if rank[x]==rank[y]: # same depth
      parent[y]=x # add group y into group x
      rank[x]+=1
    elif rank[x]<rank[y]:
      parent[x]=y # add group x into group y
    else: # rank[x]>rank[y]
      parent[y]=x # add group y into group x
  return
            
for _ in range(m):
  x,y=map(int,input().split())
  unite(x-1,y-1)

# update
r=[-1]*n
for ii in range(n):
  r[ii]=findroot(ii)

sum=[0]*n
for ii,rr in enumerate(r):
  sum[rr]+=diff[ii]

for ii in sum:
  if ii:
    print("No")
    return
print("Yes")
