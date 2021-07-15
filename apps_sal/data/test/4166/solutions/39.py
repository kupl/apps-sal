n, m = map(int, input().split())
a = ['*']*n


for i in range(m):

  s, c = map(int, input().split())
  if a[s-1] == '*':
    a[s-1] = c
  else:
    if a[s-1] == c:
      continue
    else:
      print(-1)
      return
  
if n >1 and a[0] == 0:
  print(-1)
  return
elif n >1 and a[0]=='*':
  a[0] = 1

  
b = [str(x) for x in a]
ans= ''.join(b)
print(ans.replace('*', '0'))
