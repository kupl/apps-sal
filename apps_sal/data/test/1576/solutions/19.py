s = input()
res = ''
for i in range(len(s) // 2):
    if len(s) % 2 == 1:
        res += s[i] + s[len(s) - i - 1]
    else:
        res += s[len(s) - i - 1] + s[i]

if (len(s) % 2 == 1):
    res += s[len(s) // 2]

print(''.join(reversed (res)))


