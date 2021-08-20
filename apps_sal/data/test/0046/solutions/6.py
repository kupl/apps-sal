from collections import defaultdict, deque, Counter, OrderedDict


def main():
    (n, m) = map(int, input().split())
    (n1, n2) = divmod(n, 5)
    (m1, m2) = divmod(m, 5)
    ans = n1 * 5 * m1 + m2 * n1 + m1 * n2
    if n2 + m2 >= 5:
        ans += n2 + m2 - 4
    print(ans)


def __starting_point():
    """sys.setrecursionlimit(400000)
    threading.stack_size(40960000)
    thread = threading.Thread(target=main)
    thread.start()"""
    main()


__starting_point()
