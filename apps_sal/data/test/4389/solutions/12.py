from sys import stdin

input = stdin.readline


def main():
    test = int(input())

    for _ in range(test):
        # n = int(input())
        # l = [int(i) for i in input().split(" ")]
        # n,k = [int(i) for i in input().split(" ")]
        # a,b,c,d = [int(i) for i in input().split(" ")]
        #
        # l = []
        # l = [int(i) for i in input().split(" ")]
        #
        # for i in l:
        #     print(i, end=' ')
        # print()

        s = input().strip()

        ns = s[0]

        for i in range(1, len(s) - 1, 2):
            ns += s[i]

        ns += s[len(s) - 1]
        print(ns)


main()
