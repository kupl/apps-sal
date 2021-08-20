import sys
n = int(input())
str = input()
str = str + '##'
i = 0
while i < n:
    if str[i] == 'e' and str[i + 1] == 'e' and (str[i + 2] != 'e') or (str[i] == 'o' and str[i + 1] == 'o' and (str[i + 2] != 'o')):
        sys.stdout.write(str[i] + str[i])
        i += 2
        continue
    if str[i] == 'e' or str[i] == 'o' or str[i] == 'i' or (str[i] == 'y') or (str[i] == 'u') or (str[i] == 'a'):
        sys.stdout.write(str[i])
        ch = str[i]
        while str[i] == ch:
            i += 1
        i -= 1
    else:
        sys.stdout.write(str[i])
    i += 1
