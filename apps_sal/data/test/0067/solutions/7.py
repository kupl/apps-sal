
def main():
    buf = input()
    buflist = buf.split()
    x = int(buflist[0])
    y = int(buflist[1])
    z = int(buflist[2])
    minimum = x - y - z
    maximum = x - y + z
    if minimum > 0 and maximum > 0:
        print('+')
    elif minimum < 0 and maximum < 0:
        print('-')
    elif minimum == 0 and maximum == 0:
        print('0')
    else:
        print('?')

def __starting_point():
    main()

__starting_point()
