s = input()
l = len(s)
max_l = 0
count = 0
lst = ['A', 'C', 'G', 'T']
for i in range(l):
  if s[i] in lst:
    count += 1
    if count > max_l:
      max_l = count
  else:
    count = 0
print(max_l)

