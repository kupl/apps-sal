s = input()
t = input()

n = len(s)
k = len(t)
for i in range(n - k, -1, -1):
    ok = True
    for j in range(k):
        if s[i + j] == '?' or s[i + j] == t[j]:
            continue
        else:
            ok = False
            break
    if ok:
        print((s[:i].replace('?', 'a') + t + s[i + k:].replace('?', 'a')))
        return
print('UNRESTORABLE')

