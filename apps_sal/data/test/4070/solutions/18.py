def count(x):
    if x == '0' or x == '4' or x == '6' or x == '9' or x == 'a' or x == 'd':
        return 1
    if x == '8' or x == 'b':
        return 2
    return 0


print(sum([count(x) for x in hex(int(input(), 10))[2:]]))
