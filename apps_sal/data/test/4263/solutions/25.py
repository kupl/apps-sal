s=list(input())
#print(s)
rmax=0
r=0
for ss in s:
  if ss in ["A","C","G","T"]:
    r+=1
  else:
    rmax=max(rmax,r)
    r=0
rmax=max(rmax,r)
print(rmax)
