def main():
    n = int(input()) + 1
    l = [True] * n
    l[0] = False
    tail = []
    for a in map(int, input().split()):
        if 0 < a < n and l[a]:
            l[a] = False
        else:
            tail.append(a)
    tail.sort()
    print(sum(abs(a - b) for a, b in zip((i for i, _ in enumerate(l) if _), tail)))


def __starting_point():
    main()

__starting_point()
