# -*-coding:utf-8-*-
import sys
input = sys.stdin.readline


def main():
    alpha_data = {}
    S = input()
    [alpha_data.update({chr(i): 0}) for i in range(97, 97 + 26)]

    for s in S:
        if s in alpha_data:
            tmp = alpha_data[s]
            tmp += 1
            alpha_data[s] = tmp
        else:
            continue
    for i, v in alpha_data.items():
        if v == 0:
            print(i)
            return
    print("None")


def __starting_point():
    main()


__starting_point()
