import sys
lines = [s.rstrip('\n') for s in sys.stdin.readlines()]
(n,) = [int(num) for num in lines.pop(0).split(' ')]


def iter_value_and_unit():
    for line in lines:
        (value, unit) = line.split(' ')
        value = float(value)
        if unit == 'BTC':
            yield (380000.0 * value)
        else:
            yield value


print(sum(iter_value_and_unit()))
