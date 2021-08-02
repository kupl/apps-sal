def diff(a, b):
    return min((int(a) - int(b) + 10) % 10, (int(b) - int(a) + 10) % 10)


def __starting_point():
    n = int(input())
    total = 0
    source = input()
    target = input()
    for i in range(len(source)):
        total += diff(source[i], target[i])
    print(total)


__starting_point()
