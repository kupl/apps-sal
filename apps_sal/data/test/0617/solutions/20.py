input_str = input()
str = '1*' + input_str + '*1'
str_len = len(str)
ans = 0

for i in range(2, str_len, 2):
    if (str[i - 1] == '*'):
        for j in range(i + 1, str_len, 2):
            if str[j] == '*':
                ans = max(ans, eval(str[:i] + '(' + str[i:j] + ')' + str[j:]))

print(ans)
