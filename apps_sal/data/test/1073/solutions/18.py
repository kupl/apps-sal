import collections
import math
n = int(input())
s = input()
ans = 0
for i in range(len(s)):
    for j in range(i, len(s)):
        t = s[i:j + 1]
        if t.count('U') == t.count('D') and t.count('L') == t.count('R'):
            ans += 1
print(ans)
