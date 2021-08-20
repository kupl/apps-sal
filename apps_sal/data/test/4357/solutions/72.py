def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(' '))


def main():
    data = sorted(Input(), reverse=True)
    print(int(str(data[0]) + str(data[1])) + data[2])


main()
