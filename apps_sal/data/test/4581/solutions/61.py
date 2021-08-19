s = input()
if s == 'ooo':
    print(1000)
elif s == 'oox' or s == 'oxo' or s == 'xoo':
    print(900)
elif s == 'oxx' or s == 'xox' or s == 'xxo':
    print(800)
else:
    print(700)
