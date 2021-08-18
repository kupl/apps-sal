from sys import stdin

input = stdin.readline


def main():
    test = int(input())

    for _ in range(test):

        s = input().strip()

        ns = s[0]

        for i in range(1, len(s) - 1, 2):
            ns += s[i]

        ns += s[len(s) - 1]
        print(ns)


main()
