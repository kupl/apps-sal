lst = input().split()
a = int(lst[0])
b = int(lst[1])
c = int(lst[2])
d = int(lst[3])

if ((abs(b - a) <= d) and (abs(c - b) <= d)) or (abs(c - a) <= d):
   print('Yes')
else:
   print('No')
