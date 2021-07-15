n=int(input())
c=list(input())
cnt=0
allcnt=c.count("R")
for i in range(allcnt):
  if c[i]=="R":
    cnt+=1
print(allcnt-cnt)
