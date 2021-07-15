s=input()
ans=''
for c in s:
  if c=='0':
    ans+='0'
  elif c=='1':
    ans+='1'
  else:
    ans=ans[:len(ans)-1]
print(ans)
