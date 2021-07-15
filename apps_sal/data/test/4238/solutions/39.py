n = input()
length = len(n)
ans=0

for i in range (length):
  ans +=int(n[i])

if ans % 9 ==0:
  print("Yes")
else:
  print("No")
