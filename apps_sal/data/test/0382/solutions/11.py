import sys


def main():
    (n, m, q) = list(map(int, input().strip().split()))
    s = input()
    t = input()
    pos = []
    for i in range(len(s)):
        if i + len(t) <= len(s) and s[i:i + len(t)] == t:
            pos.append(1)
        else:
            pos.append(0)
    sum = [0]
    for i in range(len(pos)):
        sum.append(sum[-1] + pos[i])
    for _ in range(q):
        (l, r) = list(map(int, input().strip().split()))
        r = r - len(t) + 1
        l -= 1
        if l < r:
            print(sum[r] - sum[l])
        else:
            print(0)
    return 0


def test(i):
    with open('test_{}.txt'.format(i)) as fin:
        sys.stdin = fin
        main()


def __starting_point():
    return main()


__starting_point()
