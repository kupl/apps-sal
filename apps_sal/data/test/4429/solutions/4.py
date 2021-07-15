t=int(input())
for _ in range(t):
  a=list(map(int,input().split()))
  a.sort()
  if a[1]==a[2]:
    print('YES')
    ans=[]
    ans.append(str(a[1]))
    ans.append(str(a[0]))
    ans.append(str(a[0]))
    print(' '.join(ans))
  else:
    print('NO')

