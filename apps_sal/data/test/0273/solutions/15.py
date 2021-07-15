s1,s2=input().split()
minn='zzzzzzzzzzzzzzzzz'
for i in range(1,len(s1)+1):
  for j in range(1,len(s2)+1):
    if s1[:i]+s2[:j] <minn:
      minn=s1[:i]+s2[:j]
print(minn)
