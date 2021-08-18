import math


def main():
    N = int(input())

    keta = int(math.log10(N)) + 1
    for A in range(1, int(pow(N, 0.5)) + 1):
        if N % A == 0:
            B = N // A
            keta = min(keta, int(math.log10(B)) + 1)

    print(keta)


main()
