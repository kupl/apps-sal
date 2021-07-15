N = int(input())
S = list(input())

a = list('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ')
ans = ''
for i in range(len(S)):
  ans += a[a.index(S[i]) + N]
  
print(ans)
