n = int(input())
s = input()

half = n//2

a = s[:half]
b = s[half:]

if a == b:
  print('Yes')
else: 
  print('No')
