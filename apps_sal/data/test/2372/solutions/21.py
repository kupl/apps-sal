def main():
    import sys
    input = sys.stdin.readline
    H, W = [int(x) for x in input().strip().split()]
    Ch, Cw = [int(x) + 1 for x in input().strip().split()]
    Dh, Dw = [int(x) + 1 for x in input().strip().split()]
    M = [0 for _ in range(H + 4)]
    M[0] = ['
    M[1] = ['
    M[-2] = ['
    M[-1] = ['
    for h in range(2, H + 2):
        M[h] = ['
    ans = 0
    q = set([(Ch, Cw)])
    M[Ch][Cw] = '
    dhdw = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while True:
        newq = set()
        while q:
            q_ = set()
            for h, w in q:
                if h == Dh and w == Dw:
                    print(ans)
                    return True
                newq.add((h, w))
                for dh, dw in dhdw:
                    if M[h + dh][w + dw] == '
                        continue
                    q_.add((h + dh, w + dw))
                    M[h + dh][w + dw] = '
            q = q_

        if newq:
            for h, w in newq:
                for dh in range(-2, 3):
                    for dw in range(-2, 3):
                        if M[h + dh][w + dw] == '.':
                            q.add((h + dh, w + dw))
                            M[h + dh][w + dw] = '
        if len(q):
            ans += 1
        else:
            print(-1)
            return True


def __starting_point():
    main()


__starting_point()
