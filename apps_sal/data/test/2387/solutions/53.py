def main():
    import sys
    from collections import deque
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline
    N = int(input())
    pq = deque([])
    mq = deque([])
    for n in range(N):
        s = input().strip()
        mini = 0
        dst = 0
        for ss in [1 if ss == '(' else -1 for ss in s]:
            dst += ss
            mini = min(dst, mini)
        
        if dst >= 0:
            pq.append((mini, dst))
        elif dst < 0:
            mq.append((mini - dst, mini, dst))
    pq = sorted(pq, reverse=True)
    mq = sorted(mq)
    p = 0
    for mini, dst in pq:
        if p + mini < 0:
            print('No')
            return
        p += dst
    for minimini, mini, dst in mq:
        if p + mini < 0:
            print('No')
            return
        p += dst
    if p != 0:
        print('No')
    else:
        print('Yes')

def __starting_point():
    main()
__starting_point()
