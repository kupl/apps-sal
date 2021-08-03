def read():
    return list(map(int, input().split()))


s = input()
for i in range(len(s)):
    if s[i] == '0':
        s = s[:i] + 'o' + s[i + 1:]
    elif s[i] == '1' or s[i] == 'i' or s[i] == 'I':
        s = s[:i] + 'l' + s[i + 1:]
a = []
n = int(input())
for i in range(n):
    c = input()
    for i in range(len(c)):
        if c[i] == '0':
            c = c[:i] + 'o' + c[i + 1:]
        elif c[i] == '1' or c[i] == 'i' or c[i] == 'I':
            c = c[:i] + 'l' + c[i + 1:]
    if c.capitalize() == s.capitalize():
        print('No')
        return
print('Yes')
