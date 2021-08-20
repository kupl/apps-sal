l = int(input())
com = []
for i in range(l):
    s = input()
    com += [s]


def parse(commands):
    stack = []
    adder = 0
    for s in commands:
        if s.startswith('for'):
            x = int(s.split()[1])
            stack.append((x, adder))
            adder = 0
        elif s == 'end':
            (old_x, old_adder) = stack.pop()
            adder = old_adder + adder * old_x
            if adder > 2 ** 32 - 1:
                break
        else:
            adder += 1
    return adder


adder = parse(com)
if adder > 2 ** 32 - 1:
    print('OVERFLOW!!!')
else:
    print(adder)
