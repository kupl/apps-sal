import sys

x=int(input())
for i in range(50):
  for j in range(30):
    if (3**(i+1))+(5**(j+1))==x:
      print(str(i+1) + " " + str(j+1))
      return
print(-1)
