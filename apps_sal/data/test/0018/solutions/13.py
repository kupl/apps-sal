s = input()
s += '{'
ans = ''
tmp = []
m = ['z' for i in range(len(s) + 1)]
for i in range(len(s) - 1, -1, -1):
    m[i] = min(m[i + 1], s[i])
for i in range(len(s) - 1):
    tmp.append(s[i])
    while len(tmp) and tmp[-1] <= m[i + 1]:
        ans += tmp.pop()
print(ans)
