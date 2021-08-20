import re
nice = re.compile('^10*$')


def main():
    _ = input()
    result = 0
    mul = '1'
    for s in input().split():
        if s == '0':
            return '0'
        if nice.match(s):
            result += len(s) - 1
        else:
            mul = s
    return mul + '0' * result


try:
    while True:
        print(main())
except EOFError:
    pass
