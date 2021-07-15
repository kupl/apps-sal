N=  int(input())
YN_list = []

a=0
for i in range(N):
  Di1,Di2 = input().split()
  if Di1 == Di2:
    a = a + 1
    if a >= 3:
      YN_list.append("Yes")
    else:
      YN_list.append("No")
  else:
    a = 0
    if a >= 3:
      YN_list.append("Yes")
    else:
      YN_list.append("No")

if 'Yes' in YN_list:
  print("Yes")
else:
  print("No")
