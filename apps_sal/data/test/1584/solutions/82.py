def main():
    from collections import deque
    from bisect import bisect_left

    n = int(input())
    l = sorted(map(int, input().split()))
    ld = deque(l)
    cnt = 0
    for a in range(n - 2):
        l_a = ld.popleft()
        for b in range(a + 1, n - 1):
            cnt += bisect_left(l, l_a + l[b]) - b - 1
    print(cnt)


def __starting_point():
    main()


__starting_point()
