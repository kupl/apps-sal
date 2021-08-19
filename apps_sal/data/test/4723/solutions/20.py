s = input()
n = len(s)
t = input()
m = len(t)
ans = []
for i in range(n - m + 1):
    for j in range(m):
        if s[i + j] not in [t[j], '?']:
            break
        elif j == m - 1:
            res = s[:i] + t + s[i + m:]
            ans.append(res.replace('?', 'a'))
if not ans:
    ans.append('UNRESTORABLE')
print(min(ans))
