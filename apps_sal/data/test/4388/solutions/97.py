s=input()
ans=[]
for i in range(3):
  if s[i]=='1':
    ans.append('9')
  else:
    ans.append('1')
print(''.join(ans))
