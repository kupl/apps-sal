a, b, c = [int(x) for x in input().split()] 

if abs(a - b) > abs(a - c):
   print("B")
else:
   print("A")

