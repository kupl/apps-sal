keyboard = ['qwertyuiop', 'asdfghjkl;', 'zxcvbnm,./']
dir = input()
str1 = input()
str2 = ''
a = -1 + 2 * (dir == 'R')
for sym in str1:
    for key in keyboard:
        if sym in key:
            str2 += key[key.index(sym) - a]
print(str2)
