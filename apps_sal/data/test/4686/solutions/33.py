s = list(input())
if all(s.count(x) % 2 == 0 for x in set(s)):
  print("Yes")
else:
  print("No")
