import bisect

s = input()
t = input()
n = len(s)
s += s

pos = [[] for _ in range(26)]

for i in range(len(s)):
    pos[ord(s[i]) - ord('a')].append(i)

ans = 0
now = -1
for i in range(len(t)):
    c = ord(t[i]) - ord('a')
    j = bisect.bisect_right(pos[c], now)

    if j == len(pos[c]):
        print((-1))
        return
    now = pos[c][j]

    if now >= n:
        now -= n
        ans += n
print((ans + now + 1))

