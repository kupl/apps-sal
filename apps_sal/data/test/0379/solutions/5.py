n,m=map(int, input().split())
flag=False
s1=''
for i in range(n):
  s=input()
  if s.find('X')>-1:
    if s1=='':
      s1=s
      flag=True
    elif s1==s:
      flag=True
    else:
      flag=False
      break
if flag:
  print('YES')
else:
  print('NO')
