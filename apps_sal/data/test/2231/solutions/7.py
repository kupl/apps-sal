from sys import stdout, stdin
import collections


def read():
    return stdin.readline().rstrip('\n')


def read_array(sep=None, maxsplit=-1):
    return read().split(sep, maxsplit)


def read_int():
    return int(read())


def read_int_array(sep=None, maxsplit=-1):
    return [int(a) for a in read_array(sep, maxsplit)]


def write(*args, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    stdout.write(sep.join(str(a) for a in args) + end)


def write_array(array, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    stdout.write(sep.join(str(a) for a in array) + end)


def f(a, b):
    return a / b + b / a


n = read_int()
results = []
for _ in range(n):
    read_int()
    arr = collections.Counter(read_int_array(sep=' '))
    prev_el, next_el = None, None
    min_sticks_el = None
    min_sticks = None
    keys = sorted(arr.keys())
    for k in keys:
        if arr[k] > 4:
            arr[k] = 4
        while arr[k] > 1:
            arr[k] -= 2
            prev_el, next_el = next_el, k
            if prev_el and next_el:
                if not min_sticks_el:
                    min_sticks_el = (prev_el, next_el)
                    min_sticks = f(prev_el, next_el)
                    continue
                current_value = f(prev_el, next_el)
                if min_sticks > current_value:
                    min_sticks = current_value
                    min_sticks_el = (prev_el, next_el)
    results.append("{0} {0} {1} {1}".format(min_sticks_el[0], min_sticks_el[1]))

print('\n'.join(results))
