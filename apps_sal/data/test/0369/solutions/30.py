import sys


def solve():
    input = sys.stdin.readline
    (N, M) = map(int, input().split())
    S = input().strip('\n')
    now = N
    ans = []
    while now > 0:
        for i in reversed(range(1, M + 1)):
            if now - i < 0:
                continue
            elif S[now - i] == '0':
                ans.append(i)
                now -= i
                break
        else:
            print(-1)
            break
    else:
        A = [int(ans[-1 - i]) for i in range(len(ans))]
        print(' '.join(map(str, A)))
    return 0


def __starting_point():
    solve()


__starting_point()
