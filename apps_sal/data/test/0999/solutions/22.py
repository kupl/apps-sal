"""Codeforces Round #404 (Div. 2)

B. Anton and Classes
"""


def dist_interval(a, b):
    p0, q0 = a
    p1, q1 = b
    if not (q0 <= p1 or q1 <= p0):
        return 0
    return min(abs(p1 - q0), abs(q1 - p0))


def main():
    n_chess_classes = int(input())
    chess_interval = [tuple(map(int, input().split()))
                      for _ in range(n_chess_classes)]

    m_prog_classes = int(input())
    prog_interval = [tuple(map(int, input().split()))
                     for _ in range(m_prog_classes)]

    ans = max(dist_interval(min(chess_interval, key=lambda x: x[1]),
                            max(prog_interval)),
              dist_interval(min(prog_interval, key=lambda x: x[1]),
                            max(chess_interval)))
    print(ans)


def __starting_point():
    main()

__starting_point()
