s = input()
a = s[:2]
b = s[2:]

l = ["01","02","03","04","05","06","07","08","09","10","11","12"]

if a in l and b in l:
  print("AMBIGUOUS")
elif a in l and b not in l:
  print("MMYY")
elif a not in l and b in l:
  print("YYMM")
else:
  print("NA")
