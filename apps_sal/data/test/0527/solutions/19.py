from bisect import bisect_left as bl, bisect_right as br
s, t = input(), input()
if not set(list(t)) <= set(list(s)):
    print(-1)
    return
ss = [[]for i in range(26)]
for i, v in enumerate(s):
    ss[ord(v) - 97].append(i)
nowind, loop = -1, 0
for i in t:
    ind = ord(i) - 97
    if ss[ind][-1] < nowind:
        nowind = -1
        loop += 1
    nowind = ss[ind][bl(ss[ind], nowind)] + 1
print(loop * len(s) + nowind)
