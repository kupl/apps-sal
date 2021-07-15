s = input()
a1 = int(s[:2])
a2 = int(s[2:])
if a1 in range(1, 13):
  if a2 in range(1, 13): print("AMBIGUOUS")
  else: print("MMYY")
else:
  if a2 in range(1, 13): print("YYMM")
  else: print("NA")
