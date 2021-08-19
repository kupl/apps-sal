def f(s):
    for i in range(len(s) - 1):
        if s[i] != '?' and s[i] == s[i + 1]:
            return False
    if s[0] == '?' or s[-1] == '?':
        return True
    for i in range(len(s) - 1):
        if s[i + 1] == s[i] == '?':
            return True
    for i in range(1, len(s) - 1):
        if s[i] == '?' and s[i - 1] == s[i + 1]:
            return True
    return False


input()
s = input()
if f(s):
    print('Yes')
else:
    print('No')
