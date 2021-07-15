from itertools import product

n=int(input())
if n<357:
  print(0)
  return
ans=0
for i in range(3,len(str(n))):
  ans+=3**i-3*(2**i)+3

for i in product(['3','5','7'],repeat=len(str(n))):
  if '3' in i and '5' in i and '7' in i:
    if int(int(''.join(i)))<=n:
      ans+=1
print(ans)
