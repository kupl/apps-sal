a = sorted(zip((len(input()) - 2 for i in range(4)), "ABCD"))
if 2 * a[2][0] <= a[3][0] and 2 * a[0][0] > a[1][0]:
  print(a[3][1])
elif 2 * a[2][0] > a[3][0] and 2 * a[0][0] <= a[1][0]:
  print(a[0][1])
else:
  print("C")
