s = input()
min_letter = 'z'
for k in range(len(s)):
    if min_letter < s[k]:
        print('Ann')
    else:
        print('Mike')
    min_letter = min(min_letter, s[k])
