s = input()
n = len(s)
l = []
r = []
for i in range(n):
    if s[i] == '(':
        l.append(i + 1)
    else:
        r.append(i + 1)
ans = 0
for i in range(min(len(l), len(r))):
    if l[i] < r[-i - 1]:
        ans += 1
    else:
        break
if ans:
    print(1)
    print(ans * 2)
    print(*l[:ans], *r[-ans:])
else:
    print(0)
