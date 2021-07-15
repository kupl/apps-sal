s = input()
if (s[0] == 'a' and (s[1] == '1' or s[1] == '8')) or\
    (s[0] == 'h' and (s[1] == '1' or s[1] == '8')):
    print(3)
elif s[0] in 'ah' or s[1] in '18':
    print(5)
else:
    print(8)

