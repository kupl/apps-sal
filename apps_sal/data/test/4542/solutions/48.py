a=input()+"p"
b=0
i=1
c=a[0]
while a[i]!="p":
  if a[i]!=c:
    c=a[i]
    b+=1
  i+=1
print(b)
