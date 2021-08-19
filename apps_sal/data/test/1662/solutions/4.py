import sys


def main():
    l = sys.stdin.readline()
    l = sys.stdin.readline()
    numbers = {}
    for el in l.split():
        el = int(el)
        try:
            numbers[el] = numbers[el] + 1
        except KeyError:
            numbers[el] = 1
    nr = numbers.keys()
    nr = sorted(list(set(nr)))
    count = 0
    final = []
    for n in nr:
        if numbers[n] > 0:
            final.append(n)
            numbers[n] -= 1
            count += 1
    nr = sorted(nr, reverse=True)
    for n in nr:
        if n != final[-1]:
            if numbers[n] > 0:
                final.append(n)
                numbers[n] -= 1
                count += 1
    print(count)
    for el in final[:-1]:
        print(el, end=' ')
    print(final[-1])


def __starting_point():
    main()


__starting_point()
