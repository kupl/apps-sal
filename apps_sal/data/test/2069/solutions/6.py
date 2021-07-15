from sys import stdin


def main():
    n, k = list(map(int, stdin.readline().split()))
    ar = list(map(int, stdin.readline().split()))
    lk = {ar[i] - 1: i for i in range(n)}
    pair = [-1 for _ in range(n)]
    for _ in range(k):
        x, y = list(map(int, stdin.readline().split()))
        if lk[y - 1] > lk[x - 1]:
            pair[y - 1] = max(pair[y - 1], lk[x - 1])
        else:
            pair[x - 1] = max(pair[x - 1], lk[y - 1])
    start = 0
    end = 0
    ok = True
    ans = 0
    while end < n:
        while end < n and ok:
            curr = ar[end] - 1
            if start <= pair[curr]:
                ok = False
            else:
                end += 1
        if end < n:
            while start <= pair[ar[end] - 1]:
                ans += end - start
                start += 1
        else:
            ans += (end - start + 1) * (end - start) // 2
        ok = True
    print(ans)


def __starting_point():
    main()

__starting_point()
