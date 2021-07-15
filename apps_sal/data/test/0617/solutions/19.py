str = '1*' + input() + '*1'
l = len(str)
ans = 0
for i in range(2, l, 2):
    if (str[i - 1] == '*'):
        for j in range(i + 1, l, 2):
            if str[j] == '*':
                ans = max(ans, eval(str[:i] + '(' + str[i:j] + ')' + str[j:]))
print(ans)
