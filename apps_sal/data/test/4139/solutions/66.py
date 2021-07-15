n = input()
l = len(n)
n = int(n)
data = [['0']*l for i in range(4**l)]
for i in range(4**l):
  k = i
  for j in range(l):
    a = k//4**(l-1-j)
    if a==1:
      data[i][j]='3'
    if a==2:
      data[i][j]='5'
    if a==3:
      data[i][j]='7'
    k%=4**(l-1-j)
ans = 0
for u in data:
  num = int(''.join(u))
  if num<=n:
    num = str(num)
    if '0' not in num and '3' in num and '5' in num and '7' in num:
      ans += 1
print(ans)
