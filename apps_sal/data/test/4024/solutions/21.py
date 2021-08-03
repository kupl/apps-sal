from itertools import combinations


def main():
    n, k = list(map(int, input().split()))
    s = input()
    lenf = len
    l_prev = {s}
    curS = 1
    cost = 0
    if k == 1:
        print(0)
        return
    for curlen in range(n - 1, -1, -1):
        l = set()
        for l_elem in l_prev:
            for v in combinations(l_elem, curlen):
                v = ''.join(v)
                if v in l:
                    continue
                l.add(v)
                curS += 1
                cost += n - curlen
                if curS == k:
                    print(cost)
                    return
        l_prev = l
    print(-1)


def __starting_point():
    main()


__starting_point()
