blah = input().split()
if blah[2] == 'week':
    if blah[0] == '5' or blah[0] == '6':
        print(53)
    else:
        print(52)
elif blah[0] == '31':
    print(7)
elif blah[0] == '30':
    print(11)
else:
    print(12)
