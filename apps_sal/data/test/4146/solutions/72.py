import collections as co


def __starting_point():

    n = int(input())
    A = list(map(int, input().split()))

    S = A[1::2]
    T = A[0::2]

    total_cnt = 0

    # 全体をチェック
    U = set(A)
    if len(U) == 1:
        total_cnt = len(A[1::2])
        print(total_cnt)
        return

    c1 = []
    c2 = []
    # 奇数列をチェック
    s = co.Counter(S)
    c1 = s.most_common()
    # これが秘策
    c1.append((0, 0))
    # 偶数列をチェック
    t = co.Counter(T)
    c2 = t.most_common()
    # これが秘策
    c2.append((0, 0))

    # チェック
    # 最頻値が異なるなら
    if c1[0][0] != c2[0][0]:
        # それ以外の数を総カウント-1
        total_cnt = len(S) - c1[0][1]
        total_cnt += len(T) - c2[0][1]
    else:
        # 最頻値が同じならその数が同じか？
        if c1[0][1] > c2[0][1]:
            total_cnt = len(S) - c1[0][1]
            total_cnt += len(T) - c2[1][1]
        elif c1[0][1] < c2[0][1]:
            total_cnt = len(S) - c1[1][1]
            total_cnt += len(T) - c2[0][1]
        else:
            # 同じ場合、２番目の数値を比較して取り換え
            if c1[1][1] > c2[0][1]:
                total_cnt = len(S) - c1[1][1]
                total_cnt += len(T) - c2[0][1]
            elif c1[1][1] < c2[1][1]:
                total_cnt = len(T) - c2[1][1]
                total_cnt += len(S) - c1[0][1]
            else:
                # どちらでもよい
                total_cnt = len(S) - c1[1][1]
                total_cnt += len(T) - c2[0][1]

    print(total_cnt)


__starting_point()
