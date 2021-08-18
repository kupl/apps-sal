s = input()
a = [0]
for i in range(len(s)):
    if s[i] == '*':
        a.append(i + 1)
a.append(len(s) + 1)
maxRes = eval(s)
for i in a:
    for j in a:
        if j > i:
            maxRes = max(maxRes, eval(s[:i] + '(' + s[i:j - 1] + ')' + s[j - 1:]))
print(maxRes)
