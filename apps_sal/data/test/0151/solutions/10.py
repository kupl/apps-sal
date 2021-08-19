s = input()
j = 0
a = ['a', 'e', 'i', 'o', 'u']
for i in range(len(s)):
    if j > 1:
        if not s[i] in a:
            if not s[i - 1] in a and (not s[i - 2] in a) and (not s[i] == s[i - 1] == s[i - 2]):
                print(' ', end='')
                j = 0
    j += 1
    print(s[i], end='')
