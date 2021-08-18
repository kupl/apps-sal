

def main():
    N = int(input())
    digits = []

    while N != 0:
        digits.append(N % 26)
        if digits[-1] == 0:
            digits[-1] = 26
            N //= 26
            N -= 1
        else:
            N //= 26
    digits.reverse()
    for d in digits:
        print(chr(96 + d), end='')
    print()


def __starting_point():
    main()


__starting_point()
