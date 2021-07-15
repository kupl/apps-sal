def main():
    S = input()
    N = len(S)
    INF = N + 1
    T = input()
    # S で i 番目の何番目の後で文字 c が出てくるかを計算
    next_loc = [[INF for _ in range(N)] for _ in range(26)]
    for i, s in enumerate(S):
        c = ord(s) - ord('a')
        next_loc[c][i - 1] = 1
    for c in range(26):
        n = INF
        for i in range(N - 1, -(N + 1), -1):
            n = min(next_loc[c][i], n + 1)
            next_loc[c][i] = n
    # 答えを計算
    ans = 0
    index = -1
    for t in T:
        c = ord(t) - ord('a')
        i = next_loc[c][index]
        if i == INF:
            print(-1)
            return
        ans += i
        index = (index + i) % N
    print(ans)


def __starting_point():
    main()
__starting_point()
