def solve():
    from collections import deque
    N, K = map(int, input().split())
    dq = deque((map(int, input().split())))
    popleft, append = dq.popleft, dq.append
    win = 0
    cur = popleft()
    while dq:
        vs = popleft()
        if cur > vs:
            win += 1
            append(vs)
        else:
            win = 1
            append(cur)
            cur = vs
        if win == K or win > N:
            print(cur)
            break


def __starting_point():
    solve()
__starting_point()
