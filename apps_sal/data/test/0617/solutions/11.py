s = input()
mults = [-1]
for i in range(len(s)):
    if s[i] == '*':
        mults.append(i)
mults.append(len(s))
max = 0
for i in range(len(mults)):
    for j in range(i + 1, len(mults)):
        news = s[:mults[i] + 1] + '(' + s[mults[i] + 1:mults[j]] + ')' + s[mults[j]:]
        v = eval(news)
        if v > max:
            max = v
print(max)
