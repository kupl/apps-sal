s=input()
tmp, ans = 0, 0
for i in range(len(s)):
  for j in range(i, len(s)):
    if all('AGCT'.count(h) == 1 for h in s[i:j +1]):
      ans = max(ans, j -i +1)
print(ans)
