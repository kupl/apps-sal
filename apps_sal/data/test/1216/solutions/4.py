abc = input()
s = '1' + input() + '1'
glas = ['a', 'e', 'i', 'o', 'u', 'y']
print(s[1], end='')
for i in range(2, len(s) - 1):
    if s[i] != s[i - 1] or s[i] not in glas:
        print(s[i], end='')
    elif (s[i] == 'o' or s[i] == 'e') and s[i + 1] != s[i] and (s[i - 2] != s[i]):
        print(s[i], end='')
