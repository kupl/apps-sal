n, l = map(int,input().split())
lst = []
for i in range(n):
  lst.append(l + i)
if (0 in lst):
  print(sum(lst))
elif (l < 0):
  print(sum(lst) - lst[n - 1])
else:
  print(sum(lst) - lst[0])
