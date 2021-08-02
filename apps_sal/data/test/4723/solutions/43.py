s = input()
t = input()

ans = 'z' * len(s)
tmp = 'z' * len(s)

x = False
for i in range(len(s) - len(t) + 1):
    ok = True
    for j in range(len(t)):
        if not (s[i + j] == '?' or s[i + j] == t[j]):
            ok = False

    if ok:
        x = True
        tmp = s[:i] + t + s[i + len(t):]
        if ans > tmp:
            ans = tmp

if x:
    ans = ans.replace("?", "a")
    print(ans)
else:
    print('UNRESTORABLE')
