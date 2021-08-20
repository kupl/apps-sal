def resolve():
    N = int(input())
    evdi = [[] for _ in range(N)]
    for i in range(N):
        cnt = int(input())
        for _ in range(cnt):
            (x, y) = list(map(int, input().split()))
            x -= 1
            evdi[i].append((x, y))
    ans = 0
    for bit in range(1 << N):
        ok = True
        for i in range(N):
            if bit >> i & 1:
                for (x, y) in evdi[i]:
                    if y == 1 and (not bit >> x & 1):
                        ok = False
                        break
                    if y == 0 and bit >> x & 1:
                        ok = False
                        break
        cnt = bin(bit).count('1')
        if ok:
            ans = max(cnt, ans)
    print(ans)


def __starting_point():
    resolve()


__starting_point()
