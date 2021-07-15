a = str(input())
i = 0
l = 0
o = 0
v = 0
e = 0
y = 0
u = 0
for i in range(len(a)):
 if a[i]=='i':
  i+=1
 elif a[i]=='l':
  l+=1
 elif a[i]=='o':
  o+=1
 elif a[i]=='v':
  v+=1
 elif a[i]=='e':
  e+=1
 elif a[i]=='y':
  y+=1
 elif a[i]=='u':
  u+=1
if i>=1 and l>=1 and o>=2 and v>=1 and e>=1 and y>=1 and u>=1:
 print('happy')
else:
 print('sad')
