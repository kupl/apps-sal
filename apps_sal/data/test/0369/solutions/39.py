import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def in_n():
    return int(readline())


def in_nn():
    return list(map(int, readline().split()))


def in_s():
    return readline().rstrip().decode('utf-8')


def in_nl():
    return list(map(int, readline().split()))


def in_nl2(H):
    return [in_nl() for _ in range(H)]


def in_map():
    return [s == ord('.') for s in readline() if s != ord('\n')]


def in_map2(H):
    return [in_map() for _ in range(H)]


def in_all():
    return list(map(int, read().split()))


def main():
    (N, M) = in_nn()
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
            print(-1)
            return
        else:
            ans.append(now - next)
            now = next
    ans = ans[::-1]
    print(' '.join(map(str, ans)))


def __starting_point():
    main()


__starting_point()
