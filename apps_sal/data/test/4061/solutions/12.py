s = input()
t = input()
l = 0
pre = []
suf = []
for i in range(len(s)):
    if s[i] == t[l]:
        pre.append(i)
        l += 1
    if l == len(t):
        break
l = len(t) - 1
for i in range(len(s) - 1, -1, -1):
    if s[i] == t[l]:
        suf.append(i)
        l -= 1
    if l == -1:
        break
pre.sort()
suf.sort()
ans = 0
ans = max(suf[0], len(s) - pre[-1] - 1)
for i in range(len(t) - 1):
    ans = max(ans, abs(suf[i + 1] - pre[i] - 1))
print(ans)
