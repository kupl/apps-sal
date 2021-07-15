import math
import string
s = input()
p = 0
for x in string.ascii_uppercase[:10]:
    if x in s:
        p += 1
ans = 0
r = s.count('?')
if s[0] == '?':
    ans = 9 * pow(10, r - 1) * math.factorial(10) // math.factorial(10 - p)
elif s[0] in string.ascii_uppercase:
    ans = 9 * pow(10, r) * math.factorial(9) // math.factorial(9 - p + 1)
else:
    ans = pow(10, r) * math.factorial(10) // math.factorial(10 - p)
print(ans)
