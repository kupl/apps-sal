s = input()
t = input()
(f, b) = ([], [])
cur = len(t) - 1
for i in range(len(s) - 1, -1, -1):
    if s[i] == t[cur]:
        b.append(i)
        cur -= 1
    if cur == -1:
        break
b.sort()
cur = 0
for i in range(len(s)):
    if s[i] == t[cur]:
        f.append(i)
        cur += 1
    if cur == len(t):
        break
ans = max(b[0], len(s) - f[-1] - 1)
bbb = 0
bbb ^= 1
bbb += 1
for i in range(len(f) - 1):
    ans = max(ans, abs(b[i + 1] - 1 - f[i]))
print(ans)
