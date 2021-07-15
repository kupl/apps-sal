s = input()
if len(s) == len(list(set(list(s)))):
    print('yes')
else:
    print('no')
