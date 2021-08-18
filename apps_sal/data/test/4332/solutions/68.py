import sys
def input(): return sys.stdin.readline().rstrip()


def main():
    S = input()
    ans = 'Yes' if int(S) % sum(map(int, list(S))) == 0 else 'No'
    print(ans)


def __starting_point():
    main()


__starting_point()
