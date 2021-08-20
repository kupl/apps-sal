def main():
    (n, x, m) = list(map(int, input().split()))
    ans = x
    now = x
    used = [0] * (m + 1)
    used[now] = 1
    cnt = 1
    while True:
        if cnt == n:
            print(ans)
            return
        cnt += 1
        now = now ** 2 % m
        if used[now] > 0:
            break
        used[now] = cnt
        ans += now
    start = used[now]
    ans = 0
    now = x
    cycle = 0
    startNum = 0
    for i in range(1, cnt):
        if i < start:
            ans += now
        elif i == start:
            cycle += now
            startNum = now
        else:
            cycle += now
        now = now ** 2 % m
    rem = n - start + 1
    cycleCnt = cnt - start
    roopCnt = rem // cycleCnt
    ans += roopCnt * cycle
    now = startNum
    for i in range(roopCnt * cycleCnt + start, n + 1):
        ans += now
        now = now ** 2 % m
    print(ans)


def __starting_point():
    main()


__starting_point()
