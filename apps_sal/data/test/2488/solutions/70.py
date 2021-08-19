import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def main():
    (N, D, A) = list(map(int, input().split()))
    mlist = []
    for _ in range(N):
        (x, h) = list(map(int, input().split()))
        mlist.append([x, (h + A - 1) // A])
    mlist.sort(key=lambda x: x[0])
    db = deque()
    dnotb = deque()
    left = mlist[0][0]
    ans = 0
    for monster in mlist:
        if monster[0] <= left + 2 * D:
            db.append(monster)
        else:
            dnotb.append(monster)
    ans = 0
    while db or dnotb:
        if not db:
            monster = dnotb.popleft()
            monster[1] += ans
            db.append(monster)
        bmonster = db.popleft()
        while dnotb:
            if dnotb[0][0] <= bmonster[0] + 2 * D:
                monster = dnotb.popleft()
                monster[1] += ans
                db.append(monster)
            else:
                break
        ans = max(ans, bmonster[1])
    print(ans)


def __starting_point():
    main()


__starting_point()
