k, x = map(int,input().split())
lst = []
for i in range(x - k + 1, x + k):
  if (-1000000 <= i <= 1000000):
    lst.append(i)
for i in range(len(lst)):
    print(lst[i], end = '')
    if (i != len(lst) - 1):
      print(" ", end = '')
print()

