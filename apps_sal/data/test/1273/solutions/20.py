n=int(input())
e=[[] for i in range(n)]
for i in range(n-1):
  inp=list(map(int,input().split()))
  e[inp[0]-1].append((inp[1]-1,i))
  e[inp[1]-1].append((inp[0]-1,i))

col=[0 for i in range(n-1)]
fl=[0 for i in range(n)]
s=[[0,0]]
mc=0
while len(s):
  ns=[]
  for i in s:
    fl[i[0]]=1
    cc=1
    for j in e[i[0]]:
      if not(fl[j[0]]):
        if cc==i[1]:
          cc+=1
        col[j[1]]=cc
        mc=max(mc,cc)
        ns.append([j[0],cc])
        cc+=1
  s=ns

print(mc)
for i in col:
  print(i)

