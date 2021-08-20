import re


def main():
    try:
        while True:
            input()
            a = list(map(len, [_f for _f in re.split('W+', input()) if _f]))
            print(len(a))
            print(*a)
    except EOFError:
        pass


main()
