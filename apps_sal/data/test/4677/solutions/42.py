from collections import deque


def main():
    ss = list(input())
    ans = deque([])
    for s in ss:
        if s == '0':
            ans.append(s)
        elif s == '1':
            ans.append(s)
        elif len(ans) == 0:
            pass
        else:
            ans.pop()
    print(*list(ans), sep='')


def __starting_point():
    main()


__starting_point()
