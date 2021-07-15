s=input()
hug=0
for i in range(len(s)//2):
  if s[i]!=s[len(s)-i-1]:
    hug+=1
print(hug)
