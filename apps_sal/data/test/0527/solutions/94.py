from collections import defaultdict
from bisect import bisect_right

s = input()
t = input()

n = len(s)

mp = [[] for _ in range(26)]
s += s
for i in range(len(s)):
    mp[ord(s[i]) - ord('a')].append(i)

ans = 0
now = -1
for i in range(len(t)):
    a = ord(t[i]) - ord('a')
    nxt = bisect_right(mp[a], now)
    if len(mp[a]) == nxt:
        print((-1))
        return

    now = mp[a][nxt]
    if now >= n:
        ans += n
        now -= n

print((ans + now + 1))

