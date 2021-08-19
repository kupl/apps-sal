s = input()
processed = True
i1 = 1
while i1 < len(s):
    while i1 < len(s):
        if s[i1] == '+':
            break
        i1 += 2
    if i1 >= len(s):
        break
    i2 = i1 + 2
    while i2 < len(s):
        if s[i2] == '*':
            break
        i2 += 2
    i2 = i2 - 2
    if i2 - i1 > 2:
        s1 = eval(s[i1 + 1:i2])
        s = s[:i1 + 1] + str(s1) + s[i2:]
        i1 += 4
    else:
        i1 += 2
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
