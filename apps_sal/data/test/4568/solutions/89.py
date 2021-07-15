n=int(input())
s=input()
shurui=[]
for i in range(len(s)-1):
  zenhan=s[0:i+1]
  kouhan=s[i+1:len(s)]
  kaburu=[]
  kaburu.clear()
  a=0
  for j in range(len(zenhan)):
    if kouhan.count(zenhan[j]) != 0 and kaburu.count(zenhan[j])==0:
      a+=1
      kaburu.append(zenhan[j])
  shurui.append(a)
print((max(shurui)))

