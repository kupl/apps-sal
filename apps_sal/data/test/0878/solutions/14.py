n = int(input())
a = list(map(int, input().split(" ")))
cond = True
sum = 0
for i in range(1,n):
      if (a[i-1]==2 and a[i]==3) or (a[i-1]==3 and a[i]==2):
            cond = False
            break
      elif i>1 and (a[i-2]==3 and a[i-1]==1 and a[i]==2):
            sum+=2
      elif (a[i-1]==2 and a[i]==1) or (a[i-1]==1 and a[i]==2):
            sum+=3
      else:
            sum+=4
if cond:
      print('Finite')
      print(sum)
else:
      print('Infinite')
