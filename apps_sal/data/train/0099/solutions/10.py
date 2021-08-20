import math


def main():
    n = int(input())
    line = input()
    zero = 0
    one = 0
    i = 0
    while i < n and line[i] == '0':
        zero += 1
        i += 1
    i = n - 1
    while i > -1 and line[i] == '1':
        one += 1
        i -= 1
    zr = False
    on = False
    for i in range(n):
        if line[i] == '0':
            zr = True
    for i in range(n - 1, -1, -1):
        if line[i] == '0':
            on = True
        if line[i] == '1' and on:
            zero += 1
            break
    if zero == 0 and one == 0:
        if zr:
            print(0)
        else:
            print(1)
    else:
        line = ''
        for k in range(zero):
            line += '0'
        for k in range(one):
            line += '1'
        print(line)


def __starting_point():
    t = int(input())
    for i in range(t):
        main()


__starting_point()
