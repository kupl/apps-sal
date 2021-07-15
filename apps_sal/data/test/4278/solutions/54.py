n=int(input())
howmany={}
cou=0
for i in range(n):
  s=input()
  sen=[c for c in s]
  sen.sort()
  a=''.join(sen)
  if a in howmany:
    howmany[a]+=1
    cou+=howmany[a]
  else:
    howmany[a]=0
print(cou)
