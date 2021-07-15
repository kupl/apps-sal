s=list(input())
cnt=0
bf=s[0]
for i in s[1:]:
  if i!=bf:
    cnt+=1
  bf=i
print(cnt)
