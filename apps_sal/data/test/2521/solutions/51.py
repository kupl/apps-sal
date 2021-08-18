import sys
import queue


def main():
    n = int(input())
    nnn = list(map(int, input().split()))

    ppp = nnn[:n]
    ccc = nnn[n:2 * n]
    bbb = nnn[2 * n:]

    pp_v = [0] * (n + 1)
    ppq = queue.PriorityQueue()
    for v in ppp:
        ppq.put(v)

    pre = sum(ppp)
    pp_v[0] = pre
    for i, v in enumerate(ccc):
        ppq.put(v)
        t = ppq.get()
        pre = pre + v - t
        pp_v[i + 1] = pre

    bb_v = [0] * (n + 1)
    bbq = queue.PriorityQueue()
    for v in bbb:
        bbq.put(-v)

    pre = -1 * sum(bbb)
    bb_v[0] = pre
    for i, v in enumerate(ccc[::-1]):
        bbq.put(-v)
        t = bbq.get()
        pre = pre + (-v) - (t)
        bb_v[i + 1] = pre

    dd = [p + q for p, q in zip(pp_v, bb_v[::-1])]
    ans = max(dd)

    print(ans)


isTest = False


def pa(v):
    if isTest:
        print(v)


def __starting_point():
    if sys.platform == 'ios':
        sys.stdin = open('inputFile.txt')
        isTest = True
    else:
        pass

    ret = main()
    if ret is not None:
        print(ret)


__starting_point()
