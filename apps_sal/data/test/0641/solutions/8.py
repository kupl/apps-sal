args = input().split()

num = int(args[0])

if args[2] == 'month':
    if num <= 29:
        print(12)
    elif num == 30:
        print(11)
    else:
        print(7)
else:
    if (num == 5) or (num == 6):
        print(53)
    else:
        print(52)
