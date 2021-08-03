s = input()
res = ['0'] * len(s)
stk = []
for i in range(len(s)):
    if s[i] == '0':
        if len(stk) > 0:
            res[stk[-1]] = '1'
            stk.pop()
    else:
        stk.append(i)
print(''.join(res))
