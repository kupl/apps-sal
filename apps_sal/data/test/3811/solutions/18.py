"""
author @ Mobarak Hosen Shakil
Dept. of ICE, Islamic University
Kushtia, Bangladesh

"""


def divisors(a, b):
    Divisors = []

    i = 2

    while(i * i <= a):
        if a % i == 0:
            Divisors.append(i)
            while(a % i == 0):
                a /= i
        i += 1

    i = 2

    while (i * i <= b):
        if b % i == 0:
            if i not in Divisors:
                Divisors.append(i)
            while (b % i == 0):
                b /= i
        i += 1

    if a != 1:
        Divisors.append(int(a))
    if b != 1 and b not in Divisors:
        Divisors.append(int(b))

    # print(Divisors)

    return Divisors


def main():

    n = int(input())

    A = list()

    for i in range(0, n):
        b = list(map(int, input().split()))
        A += b

    Prime = divisors(A[0], A[1])

    ans = -1

    for i in range(0, len(Prime)):
        Ok = 1
        for j in range(1, n):
            if A[j * 2] % Prime[i] != 0 and A[2 * j + 1] % Prime[i] != 0:
                # print(Prime[i])
                Ok = 0
                break
        if (Ok != 0):
            ans = Prime[i]
            break

    print(ans)


main()
