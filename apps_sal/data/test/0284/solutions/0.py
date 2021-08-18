3


def main():
    n = int(input())
    ans = False
    for a in range(0, 1001):
        for b in range(0, 1001):
            left = n - 1234567 * a - 123456 * b
            if left >= 0 and left % 1234 == 0:
                ans = True
    print("YES" if ans else "NO")


main()
