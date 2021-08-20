import sys
read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    (N, M) = list(map(int, input().split()))
    S = list(input())
    if S[N] == '1' or S[0] == '1':
        print(-1)
    else:
        ans = []
        now = N
        while now > 0:
            for i in range(M, 0, -1):
                j = max(now - i, -1)
                if j >= 0 and S[j] == '0':
                    ans.append(i)
                    now = j
                    break
                else:
                    continue
            else:
                print(-1)
                break
        else:
            print(' '.join(map(str, reversed(ans))))


def __starting_point():
    main()


__starting_point()
