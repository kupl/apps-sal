h,w=map(int,input().split())
a=['.'*(w+2)]
s=['.'+input()+'.' for _ in range(h)]
s=a+s+a
f=True
for i in range(1,h+1):
  for j in range(1,w+1):
    if s[i][j]=='#' and s[i][j-1]=='.' and s[i][j+1]=='.' and s[i-1][j]=='.' and s[i+1][j]=='.':
      f=False
if f:
  print('Yes')
else:
  print('No')
