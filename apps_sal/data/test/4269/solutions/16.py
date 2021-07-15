S=input()
number=[str(i)*2 for i in range(0,10)]

for j in number:
  if j in S:
    print('Bad')
    return
else:
  print('Good')

