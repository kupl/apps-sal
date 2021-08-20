a = input()
b = input()
len_a = len(a)
len_b = len(b)
if len_a > len_b:
    print('GREATER')
elif len_a < len_b:
    print('LESS')
elif a > b:
    print('GREATER')
elif a < b:
    print('LESS')
else:
    print('EQUAL')
