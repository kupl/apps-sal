s = '1*' + input() + '*1'
muls = [1]
for i in range(3, len(s) - 2, 2):
    if s[i] == '*' and (s[i - 2] == '+' or s[i + 2] == '+'):
        muls.append(i)
muls.append(len(s) - 2)
m = eval(s)
for i in range(len(muls)):
    for j in range(i + 1, len(muls)):
        (a, b) = (muls[i], muls[j])
        new_s = s[:a + 1] + '(' + s[a + 1:b] + ')' + s[b:]
        m = max(m, eval(new_s))
print(m)
