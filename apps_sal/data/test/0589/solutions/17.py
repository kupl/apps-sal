import sys
s = input()

use = [0] * 30
diff = 0
for i in s:
  c = ord(i) - ord('A')
  if (0 <= c and c <= 25): use[c] = True
for i in range(0, 30):
  if (use[i]): diff += 1
ans = 1
for i in range(10, 10 - diff, -1):
  if (i == 10 and (ord('A') <= ord(s[0]) and ord(s[0]) <= ord('Z'))): ans *= 9
  else: ans *= i
j = 0
for i in s:
  if (i == '?'):
    if (j == 0): ans *= 9
    else: ans *= 10
  j += 1
print(ans)
