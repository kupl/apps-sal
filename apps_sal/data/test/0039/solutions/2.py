
import sys
input = sys.stdin.readline

s = (input()).strip()

ans = 0

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        t = s[i:j]
        if t == t[::-1]:
            continue
        ans = max(ans, len(t))
print(ans)
