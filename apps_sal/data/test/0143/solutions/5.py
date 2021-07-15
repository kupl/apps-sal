from collections import defaultdict, deque, Counter, OrderedDict

def main():
    n = int(input())
    l = sorted([int(i) for i in input().split()])
    c = 1
    for i in l:
        if i >= c:
            c += 1
    print(c)












def __starting_point():
    """sys.setrecursionlimit(400000)
    threading.stack_size(40960000)
    thread = threading.Thread(target=main)
    thread.start()"""
    main()
__starting_point()
