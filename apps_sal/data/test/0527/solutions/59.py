import string
import bisect
s = input()
t = input()
S = [[] for _ in range(26)]
a = string.ascii_lowercase
now = -1
ans = -1
count = 0
for i in range(len(s)):
    for j in range(26):
        if s[i] == a[j]:
            S[j].append(i)
            break
for i in range(len(t)):
    for j in range(26):
        if t[i] == a[j]:
            break
    if len(S[j]) == 0:
        break
    nex = bisect.bisect_right(S[j], now)
    if nex == len(S[j]) or now >= S[j][nex]:
        count += 1
        now = S[j][0]
    else:
        now = S[j][nex]
    if i == len(t) - 1:
        ans = count * len(s) + now + 1
print(ans)
