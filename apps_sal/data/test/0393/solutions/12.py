def check(s):
    s = '0' + s + '0'
    for i in range(1, len(s) - 1):
        if s[i] == '1' and (s[i - 1] == '1' or s[i + 1] == '1'):
            return False
        if s[i] == '0' and s[i - 1] == '0' and s[i + 1] == '0':
            return False
    return True

n = int(input())
s = input()
if check(s):
    print('Yes')
else:
    print('No')

