N=int(input())
S=[]
for x,y in zip(map(int,input().split()), range(1,N+1)):
 if x==y: S.append(y)

S.append('$')
L=len(S)

l=[S[0]]
i=1
a=0
while i<L:
  if S[i]=='$':a+=1
  elif l[0]+1!=S[i]:
     a+=1
     l=[S[i]]
  else:l.append(S[i])
  i+=1
print(a)
