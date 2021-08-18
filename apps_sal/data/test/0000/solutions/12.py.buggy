s = input()
i = s.find('[')
if i == -1:
    print(-1)
    return
s = s[i:]
i = s.rfind(']')

if i == -1:
    print(-1)
    return
s = s[:i + 1]
l, h = 0, 0
for i, d in enumerate(s):
    if d == ':':
        l = i
        break
for i, d in enumerate(s):
    if d == ':':
        h = i
if l == h:
    print(-1)
    return
c = 0
for i in range(l + 1, h):
    if s[i] == '|':
        c += 1
print(c + 4)
