s = input()

lst1 = []
for i in range(len(s)):
   lst1.append(s[i])
lst1.sort()

lst2 = list(set(lst1))
lst2.sort()

if lst1 == lst2:
   print('yes')
else:
   print('no')
