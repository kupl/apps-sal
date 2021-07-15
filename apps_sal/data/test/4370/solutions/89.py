a, b = list(map(int, input().split()))
if max(a, b) - min(a, b)  <= 1:
  print("Yay!")
else:
  print(":(")

