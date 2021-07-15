s = str(input())
con = 0
con2 = 0
ans = 0
ans2 = 0
for i in range(len(s)):
  if i % 2 == 0:
    ans += 1
    if s[i] == '0':
      con += 1
  else:
    ans2 += 1
    if s[i] == '1':
      con2 += 1
L = [con + con2, (ans - con) + (ans2 - con2)]
print((min(L)))

