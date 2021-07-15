s = list(input())
for i in range(len(s)):
  s.pop(-1)
  if len(s)%2 == 1:
    continue
  if s[:len(s)//2] == s[len(s)//2:]:
    print(len(s))
    break
