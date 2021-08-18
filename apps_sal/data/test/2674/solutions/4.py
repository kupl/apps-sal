from sys import stdin, stdout


def main():
    cases = stdin.readline()
    if(int(cases[2]) ^ int(cases[1]) ^ int(cases[0])):
        print("Inclusive")
        return
    print("Exclusive")


def __starting_point():
    main()


__starting_point()
