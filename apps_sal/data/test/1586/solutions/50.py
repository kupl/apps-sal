import sys
pin = sys.stdin.readline


def main():
    N = int(pin())
    if N % 2 == 1:
        print((0))
    else:
        ans = 0
        i = 10
        while True:
            if N < i:
                break
            ans += N // i
            i *= 5
        print(ans)
    return


main()
