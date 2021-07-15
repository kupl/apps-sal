s=list(input())

num_g=num_p=0
answer=0
for i in range(len(s)):
  if num_g==num_p:
    num_g+=1
    if s[i]=="p":
      answer-=1
  else:
    num_p+=1
    if s[i]=="g":
      answer+=1

print(answer)
