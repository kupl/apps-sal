e = '1*' + input() + '*1'
l = len(e)
a = 0
for i in range(2, l, 2):
    if (e[i - 1] == '*'):
        for j in range(i + 1, l, 2):
            if e[j] == '*':
                a = max(a, eval(e[:i] + '(' + e[i:j] + ')' + e[j:]))
print(a)
