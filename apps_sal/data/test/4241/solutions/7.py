s=input()
t=input()
box=[]
for i in range(len(s)-len(t)+1):
  a=0
  for j in range(len(t)):
    if t[j]!=s[i+j]:
      a+=1
  box.append(a)
print(min(box))
