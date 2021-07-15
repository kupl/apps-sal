import sys


def main():
    s, v1, v2, t1, t2 = list(map(int, sys.stdin.readline().split()))
    a1 = t1 * 2 + v1 * s
    a2 = t2 * 2 + v2 * s
    if a1 < a2:
        print("First")
    elif a2 < a1:
        print("Second")
    else:
        print("Friendship")


main()

