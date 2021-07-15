a = []
for i in range(5):
  a.append(int(input()))
b = int(input())
if a[4] - a[0] > b:
  print(":(")
else:
  print("Yay!")


