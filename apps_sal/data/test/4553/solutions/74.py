A,B = list(map(int,input().split()))
L = ['0','1','2','3','4','5','6','7','8','9']
s = str(input())
for i in range(len(s)):
  if i == A:
    if s[A] != '-':
      print('No')
      return
  else:
    b = s[i]
    if b not in L:
      print('No')
      return
print('Yes')
      

