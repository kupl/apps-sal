import heapq


def main():
    N, M = list(map(int, input().split(' ')))
    S = input()
    T = S[::-1]
    dp = [-1] * (N + 1)
    que = [0] * M
    for i, t in enumerate(T):
        if i == 0:
            dp[0] = 0
            continue
        if len(que) == 0:
            print((-1))
            return
        index = heapq.heappop(que)
        if t == '1':
            continue
        dp[i] = 1 + dp[index]
        while len(que) < M:
            heapq.heappush(que, i)
    dp.reverse()
    path = list()
    target = dp[0] - 1
    cnt = 0
    for i in range(N + 1):
        if dp[i] != target:
            cnt += 1
        else:
            path.append(cnt)
            cnt = 1
            target -= 1
    print((' '.join(map(str, path))))


def __starting_point():
    main()


__starting_point()
