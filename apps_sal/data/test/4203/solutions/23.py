# -*-coding:utf-8-*-
import sys
input = sys.stdin.readline


def main():
    s = input()
    if s[0] != "A":
        print("WA")
        return
    if s[2:-2].count('C') != 1:
        print("WA")
        return
    s = s.replace('A', '')
    s = s.replace('C', '')
    if s.islower() == False:
        print("WA")
        return
    else:
        print("AC")


def __starting_point():
    main()


__starting_point()
