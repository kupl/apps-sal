n = int(input())
s = input()

p = s[0]
ans = s[0]
for w in s:
  if p != w:
    ans += w
  p = w
print(len(ans))
