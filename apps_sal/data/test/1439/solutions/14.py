def main():
    n, m = list(map(int, input().split()))
    l = [False] * m
    l1 = l.copy()
    for i in map(int, input().split()):
        i %= m
        l1[i] = True
        for j, f in enumerate(l, i - m):
            if f:
                l1[j] = True
        if l1[0]:
            print("YES")
            return
        l = l1.copy()
    print("NO")


def __starting_point():
    main()

__starting_point()
