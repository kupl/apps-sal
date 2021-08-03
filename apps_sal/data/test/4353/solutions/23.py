#!/usr/bin/env python3
# coding:utf-8

def main():
    stdIn = input()
    stdOut = solve(stdIn)
    print(stdOut)


def solve(stdIn):
    return stdIn.replace(',', ' ')


def __starting_point():
    main()


__starting_point()
