n=int(input())
for i in range(26):
  ans=0
  ans+=4*i
  for j in range(15):
    ans+=7*j
    if ans==n:
      print("Yes")
      return

print("No")
