totalArray=[]
answer ='No'
Yoko=False
tate=False
for i in range(3):
  array=input().split(' ')
  for j in range(len(array)):
    totalArray.append(int(array[j]))
if (totalArray[1]-totalArray[0]) == (totalArray[4]-totalArray[3]) == (totalArray[7]-totalArray[6]) and (totalArray[2]-totalArray[1]) == (totalArray[5]-totalArray[4]) == (totalArray[8]-totalArray[7]):
  Yoko=True
if (totalArray[3]-totalArray[0]) == (totalArray[4]-totalArray[1]) == (totalArray[5]-totalArray[2]) and (totalArray[6]-totalArray[3]) == (totalArray[7]-totalArray[4]) == (totalArray[8]-totalArray[5]):
  tate=True
if Yoko==True and tate==True:
  print('Yes')
else:
  print('No')
