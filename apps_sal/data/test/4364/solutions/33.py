n = int(input())

r = n // 100
l = n % 100

if r <= 12 and 1 <= r:
  if l <= 12 and 1 <= l:
    print("AMBIGUOUS")
  else:
    print("MMYY")
else:
  if l <= 12 and 1 <= l:
    print("YYMM")
  else:
    print("NA")
