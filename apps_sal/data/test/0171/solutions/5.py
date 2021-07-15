s = input()
print('Correct' if len(s) >= 5 and any([elem.isupper() for elem in s]) and any([elem.islower() for elem in s]) and any([elem.isdigit() for elem in s]) else 'Too weak')
