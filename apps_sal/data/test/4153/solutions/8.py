s = input()
n = len(s)
a = s.count('1')
b = s.count('0')
if a>=b:
  print(b*2)
else:
  print(a*2)
