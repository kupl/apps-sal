k = int(input())
a, b = list(map(int,input().split()))
list1 = []
x =(k+a-1)//k
y = b // k

for i in range(x,y+1):
  list1.append(i)
if list1 == []:
  print('NG')
else:
  print('OK')

