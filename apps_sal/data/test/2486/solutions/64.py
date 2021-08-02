def d_no_need(N, K, A):
    from bisect import bisect_left
    # 値がK以上の要素は単体で不必要でない要素になれる
    A.sort()
    a_sorted = A[:bisect_left(A, K)]
    ans = len(a_sorted)  # a_sortedの要素は不必要となりうる

    dp = [False] * K  # dp[k]:a_sortedの一部の和を取った値をKにできるか？
    dp[0] = True
    current_max = 0
    for idx, a in reversed(list(enumerate(a_sorted))):
        if current_max + a >= K:
            ans = idx  # これを満たさないaは不必要

        # current_maxはループの中で1回だけ更新する。
        # jを変化させるたびに代入すると時間がかかるため
        updated = True
        for j in range(min(current_max, K - a - 1), -1, -1):
            if dp[j]:
                dp[j + a] = True  # 和をjにできているなら、j+aにもできる
                if updated:
                    current_max = max(current_max, j + a)
                    updated = False
    return ans


N, K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
print((d_no_need(N, K, A)))
# https://beta.atcoder.jp/contests/arc070/submissions/2980516 参考
# https://medaka.5ch.net/test/read.cgi/prog/1534548265/ の>>75によると
# 8 100
# 1 1 8 8 8 25 26 50
# に対して2や5を返すsubmissionが見られるとのこと(実際は0)
