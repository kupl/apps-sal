def main():
    buf = input()
    n = int(buf)
    command = []
    for i in range(n):
        buf = input()
        buflist = buf.split()
        if len(buflist) == 2:
            buflist[1] = int(buflist[1])
        command.append(buflist)
    x = []
    for i in range(n):
        x.append(0)
    stack = []
    nest = 0
    for c in command:
        if c[0] == 'for':
            stack.append(c[1])
            nest += 1
        elif c[0] == 'add':
            x[nest] += 1
        else:
            x[nest - 1] += x[nest] * stack.pop()
            x[nest] = 0
            nest -= 1
        if x[nest] >= int(2 ** 32):
            print('OVERFLOW!!!')
            return
    print(x[0])


def __starting_point():
    main()


__starting_point()
