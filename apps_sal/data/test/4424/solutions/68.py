n = input()
x = n.split()
if 500 * int(x[0]) >= int(x[1]):
    print('Yes')
elif 500 * int(x[0]) < int(x[1]):
    print('No')
