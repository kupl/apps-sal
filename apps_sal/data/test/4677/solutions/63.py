# cook your dish here
s = str(input())
a = ""
for i in s:
  if i!='B':
    a = a + i
  else:
    if len(a)!=0:
      a = a[0:len(a)-1]
print(a)
