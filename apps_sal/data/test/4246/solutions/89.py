s=input()
t=input()

answer=0

for i in range(3):
  if s[i]==t[i]:
    answer+=1
print(answer)
