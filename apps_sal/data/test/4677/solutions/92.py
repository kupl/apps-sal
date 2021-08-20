s = list(input())
res = []
for i in range(len(s)):
    if s[i] == '1':
        res.append('1')
    elif s[i] == '0':
        res.append('0')
    elif res == []:
        continue
    else:
        del res[-1]
print(''.join(res))
