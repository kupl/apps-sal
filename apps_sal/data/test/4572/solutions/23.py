s = input()
ans = 'None'
line = [0 for i in range(26)]
for i in s:
  line[ord(i)-97] += 1
for j in range(26):
  if line[j] == 0:
    ans = chr(j + 97)
    break
print(ans)
