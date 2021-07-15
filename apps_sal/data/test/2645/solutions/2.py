s=input()
count=0
for i in range(len(s)):
  if i % 2 == 0:
    if s[i]=='p':
      count -= 1
  else:
    if s[i]=='g':
      count += 1

print(count)
