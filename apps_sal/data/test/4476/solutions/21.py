import sys
input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        a, b = map(int, input().split())
        if a == b:
            print(0)
            continue
        if a < b:
            if a % 2 == b % 2:
                print(2)
            else:
                print(1)

        else:
            if a % 2 == b % 2:
                print(1)
            else:
                print(2)


main()
