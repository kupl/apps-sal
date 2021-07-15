#!/usr/bin/env python3

def main():
    n = input()
    s = list(map(int, input()))
    t = list(s)
    c = 1
    for i in range(len(t)):
        if c == 0:
            break
        t[i] += 1
        if t[i] == 2:
            t[i] = 0
            c = 1
        else:
            c = 0
    res = 0
    for i in range(len(t)):
        res += (t[i] != s[i])
    print(res)

def __starting_point():
    main()

__starting_point()
