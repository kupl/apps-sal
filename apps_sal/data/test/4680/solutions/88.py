a = list(map(int,input().split()))
num_5 = 0
num_7 = 0

for i in a:
  if i==5:
    num_5 = num_5+1
  if i==7:
    num_7 = num_7+1

if num_5==2 and num_7==1:
  print("YES")
else:
  print("NO")
