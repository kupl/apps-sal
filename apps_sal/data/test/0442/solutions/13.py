r = int(input())

if r % 2 == 0:
  print("NO")
else:
  k = (r - 1) // 2 - 1
  if k > 0:
    print(1, k)
  else:
    print("NO")
