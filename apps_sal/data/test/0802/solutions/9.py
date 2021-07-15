def createdict():
  x={}
  for i in range(26):
    x[chr(ord('a')+i)]=i
  for i in range(26,52):
    x[chr(ord('A')+i-26)]=i
  return x

n=int(input().strip())
s=input().strip()
l=[[] for i in range(52)]
ts=set()
cs=set()
d=createdict()

for i in range(n):
  if s[i] not in ts:
    ts.add(s[i])
  l[d[s[i]]].append(i)

for end in range(n):  # start = 0
  if s[end] not in cs:
    cs.add(s[end])
  if ts&cs == ts:
    break

ans=end+1
flag=0

for start in range(1,n):
  c=s[start-1]
  while l[d[c]]:
    if l[d[c]][0]<start:
      del l[d[c]][0]
      if len(l[d[c]])==0:
        flag=1
    elif start<=l[d[c]][0]<=end:
      break
    else:
      end=l[d[c]][0]
      break
  if flag:
    break
  ans=min(ans,end-start+1)
  
print(ans)
