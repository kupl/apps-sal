import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: list(map(int, readline().split()))
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: list(map(int, read().split()))


def main():
    N, M = in_nn()
    S = in_s()

    ans = []
    now = N
    while now > 0:
        next = -1
        end = max(0, now - M)
        for i in range(now - 1, end - 1, -1):
            if S[i] == '0':
                next = i
        if next == -1:
            print((-1))
            return
        else:
            ans.append(now - next)
            now = next

    ans = ans[::-1]
    print((' '.join(map(str, ans))))


def __starting_point():
    main()

__starting_point()
