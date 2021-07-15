from collections import Counter
a = Counter(input()).most_common()
if len(a)==2:
  if a[1][1]==2:
    print("Yes")
else:
  print("No")
