s = input()
yes = False
try:
    ab = s.index('AB')
    ba = s.rindex('BA')
    if ba - ab > 1:
        yes = True
    ab = s.index('BA')
    ba = s.rindex('AB')
    if ba - ab > 1:
        yes = True
except ValueError:
    pass
print('YES' if yes else 'NO')
