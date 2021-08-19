import sys


def ReadInput():
    return sys.stdin.read().splitlines()


def GetIA(s, delim=' '):
    return [int(x) for x in s.split(delim)]


def GetKey(flags):
    key = 0
    for a in flags:
        key <<= 1
        key += a
    return key


def main():
    input = ReadInput()
    seen = dict()
    for s in input[1:]:
        seen[GetKey(GetIA(s))] = True
    for a in seen.keys():
        for b in seen.keys():
            if a & b == 0:
                print('YES')
                return
    print('NO')


main()
