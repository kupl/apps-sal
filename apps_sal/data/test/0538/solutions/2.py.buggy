s = input()
i = len(s) - 1
while s[i] == '0':
    i -= 1
s = s[:(i + 1)]
for i in range(len(s) // 2):
    if s[i] != s[len(s) - i - 1]:
        print('NO')
        return
print('YES')
