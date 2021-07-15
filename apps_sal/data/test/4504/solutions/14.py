s = input()
n = len(s)

for i in range(n // 2 - 1):
  s = s[:len(s)-2]
  if s[:len(s)//2] == s[len(s)//2:]:
    print(len(s))
    break
