num = int(input())
num = str(num)
n = list(map(int, num))
S = 0
for i in range(len(n)):
  S += int(n[i])
  
num = int(num)
if num%S==0:
  print('Yes')
else:
  print('No')
