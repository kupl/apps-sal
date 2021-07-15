h,w=list(map(int,input().split()))
masu=[]
masu.append([])
for i in range(w+2):
  masu[0].append('.')
for i in range(h):
  masu.append([])
  masu[i+1].append('.')
  yoko=input()
  for j in range(w):
    masu[i+1].append(yoko[j])
for i in range(w+2):
  masu[0].append('.')
for i in range(1,h-1):
  for j in range(1,w-1):
    if masu[i][j]=='#':
      if masu[i][j+1]=='.' and masu[i][j-1]=='.' and masu[i+1][j]=='.' and masu[i-1][j]=='.':
        print('No')
        return
print('Yes')
