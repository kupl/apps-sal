from collections import defaultdict


def main():
    n = int(input())
    shelf = map(int, input().split())
    oper = map(int, input().split())
    d = defaultdict(int)
    for (i, book) in enumerate(shelf, 1):
        d[book] = i
    top = 1
    for cur in oper:
        remIndex = d[cur]
        ans = remIndex - top + 1
        if ans <= 0:
            print('0', end=' ')
        else:
            print(ans, end=' ')
            top = remIndex + 1


main()
