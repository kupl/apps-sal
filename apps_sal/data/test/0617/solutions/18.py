s = input()
t = len(s)
res = eval(s)
for i in range(0, t):
    if i != 0 and s[i - 1] != '*':
        continue
    a = s[:i] + '(' + s[i:]
    for j in range(i, t + 2):
        if j != t + 1 and a[j] != '*':
            continue
        if j == t + 1:
            b = a[:j] + ')'
        else:
            b = a[:j] + ')' + a[j:]
        res = max(res, eval(b))
print(res)
