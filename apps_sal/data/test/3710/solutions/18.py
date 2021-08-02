import math


def main():
    n, k = list(map(int, input().split()))
    C = list(map(int, input().split()))
    l = C[0]
    for c in C:
        l = l * c // math.gcd(l, c) % k
        if(l == 0):
            print("Yes")
            return
    print("No")


main()
