import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def getN():
    return int(input())


def getList():
    return list(map(int, input().split()))


def solve():
    nums = [int(i) for i in input().strip()]
    odds = []
    evens = []
    (lodd, leven) = (0, 0)
    for num in nums:
        if num % 2 == 1:
            odds.append(num)
            lodd += 1
        else:
            evens.append(num)
            leven += 1
    odds.append(100)
    evens.append(100)
    (io, ie) = (0, 0)
    ans = []
    while True:
        if odds[io] < evens[ie]:
            ans.append(odds[io])
            io += 1
            if io == lodd:
                ans += evens[ie:leven]
                break
        else:
            ans.append(evens[ie])
            ie += 1
            if ie == leven:
                ans += odds[io:lodd]
                break
    print(''.join(list(map(str, ans))))
    return


def main():
    t = getN()
    for times in range(t):
        solve()


def __starting_point():
    main()


__starting_point()
