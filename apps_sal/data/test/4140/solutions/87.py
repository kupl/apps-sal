s=input()
cnt=0

for i in range(len(s)):#白黒白黒...
  if i%2==0:
    if s[i]=="0":
      cnt+=1

  else:
    if s[i]=="1":
      cnt+=1

print(min(cnt,len(s)-cnt))
