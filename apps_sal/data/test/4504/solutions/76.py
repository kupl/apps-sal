import sys
S = input()

for i in range(1, len(S)):
  s = S[:-i]
  l = len(s) // 2
  if s[:l] == s[l:]:
    print((len(s)))
    return

