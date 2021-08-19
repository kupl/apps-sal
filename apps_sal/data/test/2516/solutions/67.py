from collections import defaultdict


def main():
    N, P = list(map(int, input().split()))
    S = input()
    if P in [2, 5]:
        ans = 0
        # P = 2, 5の時は一番下の位の数だけ見ればカウント可能
        for right in range(N - 1, - 1, - 1):
            if int(S[right]) % P == 0:
                ans += right + 1
        print(ans)
        return
    # 例：S = 3543, P = 3
    # 左からn番目 ～ 1番右の数のmod Pの値を計算
    #     C = [3543, 543, 43, 3] % P = [0, 0, 1, 0]
    # C[m] == C[n] なる m < nのペア数 + C[n] == 0なるnの個数を求める
    #     3 + 3 = 6
    cur_c = 0
    C = [0] * N
    pw = 1
    for n, s in enumerate(S[::-1]):
        cur_c = (cur_c + pw * int(s)) % P
        C[N - 1 - n] = cur_c
        pw = (pw * 10) % P
    counter = defaultdict(int)
    for c in C:
        counter[c] += 1
    ans = 0
    for c in C:
        counter[c] -= 1
        ans += counter[c]
    ans += len([c for c in C if c == 0])
    print(ans)


def __starting_point():
    main()


__starting_point()
