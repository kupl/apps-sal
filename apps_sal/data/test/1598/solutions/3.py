s = input()
n = len(s)
if n == 1:
    print(0)
elif n == 2:
    if s == '10':
        print('10')
    else:
        print('00')
else:
    s_lis = 0
    s_max = 0
    s_zero = 0
    t_zero = 0
    stack_01 = []
    t = []
    for i in range(n):
        t.append('0')
        t_zero += 1
        if s[i] == '0':
            s_zero += 1
        if i > 0 and s[i - 1:i + 1] == '10':
            t[i - 1] = '1'
            t_zero -= 1
            stack_01.append(i - 2)
        if s_max <= int(s[i]):
            s_lis += 1
            s_max = max(s_max, int(s[i]))
        if s_lis <= s_zero:
            s_lis = s_zero
            s_max = 0
        if s_lis < t_zero:
            while t[stack_01[-1]] == '1' or s[stack_01[-1]] == '0' or t[stack_01[-1] - 1] == '1':
                stack_01.pop()
            t[stack_01[-1]] = '1'
            t_zero -= 1
            stack_01[-1] -= 1
    print(*t, sep='')
