a = input()
b = input()
alph = [0] * 26
for i in range(26):
   alph[i] = chr(97 + i)
ans = []
for i in range(len(a)):
   if a[i] != alph[ord(b[i]) - 97]:
      if (alph[ord(a[i]) - 97] == a[i]) and (alph[ord(b[i]) - 97] == b[i]):
         alph[ord(a[i]) - 97] = b[i]
         alph[ord(b[i]) - 97] = a[i]
         ans.append((a[i], b[i]))
      else:
         print(-1)
         return
for i in range(len(b)):
   if a[i] != alph[ord(b[i]) - 97]:
      print(-1)
      return
print(len(ans))
for i in range(len(ans)):
   print(ans[i][0], ans[i][1])
