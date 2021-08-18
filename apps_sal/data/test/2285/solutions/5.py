import sys


def solve():
    n = int(input())
    for test in range(n):
        line = input().split(':')
        i = 0
        while i < len(line):
            if i > 0 and line[i] == '' and line[i - 1] == '':
                line.pop(i)
                i -= 1
            i += 1
        for i, string in enumerate(line):
            if string == '':
                line[i] = modify(string, want=(32 - 4 * (len(line) - 1)))
            else:
                line[i] = modify(string)
        tempstr = ''.join(line)
        chunked = [tempstr[i: i + 4] for i in range(0, 32, 4)]
        print(':'.join(chunked))


def modify(string, want=4):
    while len(string) < want:
        string = '0' + string
    return string


if sys.hexversion == 50594544:
    sys.stdin = open("test.txt")
solve()
