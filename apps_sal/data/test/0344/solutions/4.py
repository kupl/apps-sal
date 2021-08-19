s = input()
vowels = 'aeiou'
berl = True
for i in range(len(s) - 1):
    if s[i] not in vowels and s[i] != 'n':
        if s[i + 1] not in vowels:
            berl = False
            break
if s[-1] not in vowels and s[-1] != 'n':
    berl = False
if berl == False:
    print('NO')
else:
    print('YES')
