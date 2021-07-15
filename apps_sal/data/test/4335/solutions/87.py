import sys
n= int(input())
s = input()

if (n % 2):
  print("No")
  return

half = n//2
for i in range(half):
  if s[i] != s[i+half]:
    print("No")
    return
print("Yes")
