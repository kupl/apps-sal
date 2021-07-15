N = -int(input())
a = ""

while N:
  a+=str(N%2)
  N//=-2

if a=="":
  print(0)
else:
  print(a[::-1])
