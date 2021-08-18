S = input()
L = []
for i in range(len(S)):
    L.append(S[i])

n = len(S)
ans = []
for i in range(2 ** (n - 1)):
    obj = []
    for j in range(n - 1):
        if (i >> j) & 1:
            obj.append(j)
        else:
            obj.append(-1)
    s = ''
    s += L[0]
    for j in range(len(obj)):
        if obj[j] == -1:
            s += L[j + 1]
            continue
        else:
            s += '+'
            s += L[j + 1]
    idx = 0
    now = 0

    while True:
        if now == len(s) - 1:
            ans.append(int(s[idx:]))
            break
        if s[now] == '+':
            ans.append(int(s[idx:now]))
            idx = now + 1
            now = idx
        else:
            now += 1
print((sum(ans)))
