lst = list(map(int, input().split()))
s, m = sum(lst), max(lst)
if not (3 * m - s) % 2:
  print((3 * m - s) // 2)
else:
  print((3 * (m + 1) - s) // 2)
