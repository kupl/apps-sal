n = list(input())
x = int(n[0]+n[1])
y = int(n[2]+n[3])

if 1 <= x and x <= 12:
  if 1 <= y and y <= 12:
    print("AMBIGUOUS")
  else:
    print("MMYY")
elif 1 <= y and y <= 12:
  print("YYMM")
else:
  print("NA")
