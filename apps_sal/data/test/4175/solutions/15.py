import sys
input = sys.stdin.readline


def main():
    words = []
    n = int(input())
    words = [input().rstrip() for _ in range(n)]
    if len(set(words)) != n:
        print('No')
        return
    endstring = ''
    for word in words:
        if len(endstring) == 0:
            endstring = word[-1]
        elif endstring == word[0]:
            endstring = word[-1]
        else:
            print('No')
            return
    print('Yes')


def __starting_point():
    main()


__starting_point()
