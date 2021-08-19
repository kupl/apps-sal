import sys


def is_power2(num):
    return num != 0 and ((num & (num - 1)) == 0)


lines = [line.strip() for line in sys.stdin.readlines()]

n = int(lines[0].split(' ')[0])
a = list(map(int, lines[1].split(' ')))

is_in = {}
for i, x in enumerate(a):
    is_in[x] = i

to_stay = set()

for i, x in enumerate(a):
    for p in range(32):
        if ((2**p) - x) in is_in and is_in[((2**p) - x)] != i:
            # print(str(x) + ' + ' +str(((2**p) - x)) + '=' + str(2**p))
            to_stay.add(i)
            to_stay.add(is_in[((2**p) - x)])

print(len(a) - len(to_stay))
