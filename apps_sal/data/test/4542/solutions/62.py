s = input()
temp = s[0]
ans = 0
for l in s:
  if temp!=l:
    ans += 1
  temp = l
print(ans)
