s=input()
data=[]
for i in range(len(s)):
  if s[i]=='0':
    data.append('0')
  elif s[i]=='1':
    data.append('1')
  else:
    if len(data)==0:
      continue
    else:
      data.pop()
print(*data,sep='')
