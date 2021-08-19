# -*-coding:utf-8-*-
import sys
input = sys.stdin.readline


def main():
    answers = [0]
    n = int(input())
    S = input()
    x = 0

    for s in S:
        if "I" in s:
            x += 1
            answers.append(x)
        elif "D" in s:
            x -= 1
            answers.append(x)
    print(max(answers))


def __starting_point():
    main()


__starting_point()
