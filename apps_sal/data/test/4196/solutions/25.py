import math


def main():
    N = int(input())
    A = [int(a) for a in input().split(" ")]
    gcd1 = []
    gcd2 = []
    for i in range(len(A)):
        if i == 0:
            gcd1.append(A[0])
            gcd2.append(A[-1])
        else:
            gcd1.append(math.gcd(A[i], gcd1[-1]))
            gcd2.insert(0, math.gcd(A[-i - 1], gcd2[0]))

    gcds = []
    for i in range(N):
        if i == 0:
            gcds.append(gcd2[1])
        elif i == N - 1:
            gcds.append(gcd1[-2])
        else:
            gcds.append(math.gcd(gcd1[i - 1], gcd2[-N + i + 1]))
    print((max(gcds)))


main()
