n = int(input())
s = '?' + input() + '?'
flag = False
for x in range(1, len(s) - 1):
    if s[x] == '?':
        k = 0
        for y in ['C', 'Y', 'M']:
            if s[x - 1] != y and s[x + 1] != y:
                k += 1
        if k > 1:
            flag = True
    elif s[x - 1] == s[x] or s[x + 1] == s[x]:
        flag = False
        break
if flag:
    print('Yes')
else:
    print('No')
