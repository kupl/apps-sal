st=input()
num=int(input())
maxlen=0
for start in range(len(st)+num):
  for end in range(start+1,len(st)+num,2):
    middle=(end+start+1)//2
    ans=True
    for it in range(min(len(st)-middle,end-middle)):
      if(st[start+it]!=st[middle+it]):
        ans=False
        break
    if ans:
      maxlen=max(maxlen,end-start+1)
print(maxlen)

