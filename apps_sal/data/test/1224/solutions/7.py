n = int(input())
for a in range(1,100):
  for b in range(1,200):
    if 5**b+3**a == n:
      print(f"{a} {b}")
      return
print(-1)
