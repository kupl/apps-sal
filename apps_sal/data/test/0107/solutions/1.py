s = input()
one = False
zero = 0
for x in s:
    if not one:
        if x == '1':
            one = True
    elif x == '0':
        zero += 1
print('yes' if zero >= 6 else 'no')
