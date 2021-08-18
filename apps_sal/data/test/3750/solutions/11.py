import sys
3


def main():
    k, a, b = list(map(int, input().split()))

    if a == 0 or b == 0:
        if (a + b) % k == 0:
            print((a + b) // k)
        else:
            print(-1)
    elif a % k == 0 or b % k == 0:
        print(a // k + b // k)
    elif a // k >= 1 and b // k >= 1:
        print(a // k + b // k)
    else:
        print(-1)


main()
