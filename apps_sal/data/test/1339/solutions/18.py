from collections import defaultdict, deque, Counter, OrderedDict


def main():
    n = int(input())
    mi, ma = 10**10, -1
    l = []
    for i in range(n):
        a, b = map(int, input().split())
        mi = min(mi, a)
        ma = max(ma, b)
        l.append((a, b))

    check, ind = False, 0
    for i, v in enumerate(l):
        if check:
            break
        check |= (v[0] <= mi and v[1] >= ma)
        ind = i + 1

    print(ind if check else -1)


def __starting_point():
    """sys.setrecursionlimit(400000)
    threading.stack_size(40960000)
    thread = threading.Thread(target=main)
    thread.start()"""
    main()


__starting_point()
