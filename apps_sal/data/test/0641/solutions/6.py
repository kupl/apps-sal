line = input().split()
n = int(line[0])
if line[2] == 'month':
    if n == 31:
        print(7)
    elif n == 30:
        print(11)
    else:
        print(12)
elif n == 5 or n == 6:
    print(53)
else:
    print(52)
