def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    x, y, z = Input()

    people = x // y
    spaces = (people + 1) * z
    while True:
        if people * y + spaces <= x:
            print(people)
            return
        people -= 1
        spaces = (people + 1) * z


main()
