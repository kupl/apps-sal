import math
N = int(input())
Xlist = list(map(int,input().split()))

min =10**5
meandown = math.floor(sum(Xlist)/N)
meanup = math.ceil(sum(Xlist)/N)
sumdown=0
sumup = 0
for i in range(len(Xlist)):
  sumdown+= (Xlist[i]-meandown)**2
  sumup+= (Xlist[i]-meanup)**2
  
if sumdown<sumup:
  print(sumdown)
else:
  print (sumup)
