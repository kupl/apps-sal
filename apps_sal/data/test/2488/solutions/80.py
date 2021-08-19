from sys import stdin
from collections import deque


def main():
    # 入力
    readline = stdin.readline
    n, d, a = map(int, readline().split())
    xh = [list(map(int, readline().split())) for _ in range(n)]
    xh.sort()
    x = [0] * n
    h = [0] * n
    for i in range(n):
        x[i], h[i] = xh[i][0], xh[i][1]

    dq = deque()
    now = 0
    cnt = 0
    for i in range(n):
        if i == 0:
            cnt += (h[i] + a - 1) // a
            now += (h[i] + a - 1) // a * a
            dq.append([x[i] + 2 * d, now])
        else:
            while len(dq) != 0 and dq[0][0] < x[i]:
                tmp = dq.popleft()
                now -= tmp[1]
            if h[i] <= now:
                pass
            else:
                dq.append([x[i] + 2 * d, (h[i] - now + a - 1) // a * a])
                cnt += (h[i] - now + a - 1) // a
                now += (h[i] - now + a - 1) // a * a

    print(cnt)


def __starting_point():
    main()


__starting_point()
