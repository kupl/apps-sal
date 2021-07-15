n=int(input())
for i in range(26):
  for j in range(15):
    if n == 4*i + 7*j:
      print("Yes")
      return
print("No")
