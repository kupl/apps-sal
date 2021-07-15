A,B=map(int,input().split())
S=input()
a=S[:A]
b=S[A]
c=S[A+1:]
ans=True
for i in range(A):
  if a[i].isdigit()==False:
    print('No')
    return
if b!='-':
  print('No')
  return
for i in range(B):
  if c[i].isdigit()==False:
    print('No')
    return
print('Yes')
