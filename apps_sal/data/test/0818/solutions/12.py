
x=int(input())
if x in [1,2]:
   print(-1)
elif x==3:
   print(210)
else:
   print('1'+'0'*(x-4+3-len(str(210-pow(10,x-1,210))))+str(210-pow(10,x-1,210)))

