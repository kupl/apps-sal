s=0
m={}
o={}
n,k=map(int,input().split())
l=list(map(int,input().split()))
for a in l:
 if a%k==0:
  s+=m.get(a/k,0)
  m[a]=m.get(a,0)+o.get(a/k,0)
 o[a]=o.get(a,0)+1
print(s)
