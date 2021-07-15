def b176(n):

    intn = [int(i) for i in n]

    return "Yes" if sum(intn) % 9 == 0 else "No"


def main():
    n = list(str(input()))
    print(b176(n))

def __starting_point():
    main()
__starting_point()
