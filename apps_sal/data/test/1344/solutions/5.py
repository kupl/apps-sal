'''
def main():
    from sys import stdin,stdout
def __starting_point():
    main()
'''


def main():
    from sys import stdin, stdout
    n = int(stdin.readline())
    tup = tuple(map(int, stdin.readline().split()))
    maxim = 1
    count = 1
    for i in range(1, n):
        if tup[i] > tup[i - 1]:
            count += 1
        else:
            maxim = max(count, maxim)
            count = 1
    maxim = max(count, maxim)
    stdout.write(str(maxim))


def __starting_point():
    main()


__starting_point()
