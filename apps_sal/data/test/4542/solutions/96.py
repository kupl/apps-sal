s = input()

now = ""
ans = 0
for i in range(len(s)):
  if i == 0:
    now = s[0]
    continue
  if s[i] != now:
    ans += 1
    now = s[i]
print(ans)
