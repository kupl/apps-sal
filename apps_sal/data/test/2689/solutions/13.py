s = input().rstrip()
i = 0
final = ''
while i < len(s):
    if s[i].isdigit():
        val = int(s[i])
        s1 = ''
        while s[i] != '-':
            if s[i].isalpha():
                s1 += s[i]
            i += 1
        i += 1
        final += s1 * val
    else:
        s1 = ''
        while s[i].isalpha():
            s1 += s[i]
            i += 1
            if i >= len(s):
                break
        final += s1
final = list(final)
temp = final[::-1]
if final == temp:
    print('Return')
else:
    print('Continue')
