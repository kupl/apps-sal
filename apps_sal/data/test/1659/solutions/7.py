from collections import defaultdict, deque, Counter, OrderedDict


def main():
    n, x = map(int, input().split())
    ans = 0
    for _ in range(n):
        s = input().split()
        if s[0] == '+':
            x += int(s[1])
        else:
            if x >= int(s[1]):
                x -= int(s[1])
            else:
                ans += 1
    print(x, ans)


def __starting_point():
    """sys.setrecursionlimit(400000)
    threading.stack_size(40960000)
    thread = threading.Thread(target=main)
    thread.start()"""
    main()


__starting_point()
