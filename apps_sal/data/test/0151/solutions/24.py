s = input()
s2 = s1 = ''
l1 = {'a', 'e', 'i', 'o', 'u'}
k = 0
for i in range(len(s)):
  if s[i] not in l1:
    if k == 2:
      if s[i] != s[i-1] or s[i-1] != s[i-2]:
        print(s1 + ' ', end = '', sep = '')
        s1 = s[i]
        k = 1
      else:
        s1 += s[i]  
    else:
      k += 1
      s1 += s[i]
  else:
    k = 0
    s1 += s[i]
print(s1)
