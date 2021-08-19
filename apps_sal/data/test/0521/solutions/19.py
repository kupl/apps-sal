n = int(input())
s = input()


def f(s):
    for i in range(len(s) - 1):
        if s[i] != '?':
            if s[i] == s[i + 1]:
                return False
    for i in range(len(s)):
        if s[i] == '?':
            if i == 0 or i == len(s) - 1:
                return True
            else:
                if s[i + 1] == '?':
                    return True
                if s[i - 1] == s[i + 1]:
                    return True
    return False


if f(s):
    print('Yes')
else:
    print('No')
