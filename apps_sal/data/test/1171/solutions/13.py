import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, K = map(int, input().split())
V = list(map(int, input().split()))

ans = 0  # 何もしないと0なので、ansの初期値は0


# pick->取り出す操作をする回数(listより多く取り出さないように注意)
for pick in range(min(K + 1, N + 1)):
    # 右から取り出す数
    for right in range(pick + 1):
        left = pick - right  # 左から取り出す数
        pick_list = V[:right] + V[N - left:]

        # queueに戻す操作
        pick_list = sorted(pick_list)
        tmp_ans = sum(pick_list)  # 戻す前の合計値
        rem = min(K - pick, len(pick_list))  # 戻す操作をできる回数
        for i in range(rem):  # 負の値のものをできるだけ戻す
            if pick_list[i] < 0:
                tmp_ans -= pick_list[i]
            else:
                break
        ans = max(tmp_ans, ans)
print(ans)
