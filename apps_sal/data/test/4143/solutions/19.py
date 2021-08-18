import math


def main():
    n = int(input())
    csr = []
    for _ in range(5):
        csr.append(int(input()))
    print((4 + math.ceil(n / min(csr))))


def __starting_point():
    main()


__starting_point()
