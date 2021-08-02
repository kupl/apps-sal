from collections import defaultdict


def main(n):
    tr = {0: 2, 1: 7, 2: 2, 3: 3, 4: 3, 5: 4, 6: 2, 7: 5, 8: 1, 9: 2}
    print(tr[int(n[0])] * tr[int(n[1])])
    return
    mx = -99999999999
    a.sort()
    b.sort()
    a2 = 0  # last b 2p
    b2 = 0  # last a 2p
    for d in sorted(list(set([0] + a + b))):
        for a2 in range(a2, n + 1):
            if a2 == n or a[a2] > d: break
        for b2 in range(b2, m + 1):
            if b2 == m or b[b2] > d: break
        s1 = a2 * 2 + (n - a2) * 3
        s2 = b2 * 2 + (m - b2) * 3
        if s1 - s2 > mx:
            mx = s1 - s2
            res = "{}:{}".format(s1, s2)
    print(res)


def main_input():
    #n = int(input())
    n = input()
    #a = [int(i) for i in input().split()]
    #a = map(int, input().split())
    #m = int(input())
    #b = [int(i) for i in input().split()]
    main(n)


def __starting_point():
    main_input()


__starting_point()
