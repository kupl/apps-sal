import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines


def main():
    N = int(readline())
    a = list(map(int, readline().split()))

    ans = []
    MAX = max(a); MIN = min(a)
    if MIN >= 0:
        for i in range(1, N):
            ans.append((i, i + 1))
    elif MAX <= 0:
        for i in reversed(list(range(1, N))):
            ans.append((i + 1, i))
    elif MAX > -MIN:
        max_idx = a.index(MAX)
        for i in range(N):
            if a[i] < 0:
                ans.append((max_idx + 1, i + 1))
        for i in range(1, N):
            ans.append((i, i + 1))
    else:
        min_idx = a.index(MIN)
        for i in range(N):
            if a[i] > 0:
                ans.append((min_idx + 1, i + 1))
        for i in reversed(list(range(1, N))):
            ans.append((i + 1, i))

    print((len(ans)))
    for i, j in ans:
        print((i, j))


def __starting_point():
    main()


__starting_point()
