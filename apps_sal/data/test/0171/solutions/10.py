s = input()
yes = True
yes &= len(s) >= 5
yes &= any(c.isupper() for c in s)
yes &= any(c.islower() for c in s)
yes &= any(c.isdigit() for c in s)

if yes:
    print('Correct')
else:
    print('Too weak')

