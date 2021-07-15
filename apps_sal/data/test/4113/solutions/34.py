n=int(input())

s="No"
for i in range(26):
  for j in range(15):
    if 4*i+7*j==n:
      s="Yes"
print(s)

