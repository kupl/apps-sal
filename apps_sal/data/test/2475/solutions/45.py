def f_frog_jump(N, S):
    ans = 0
    for c in range(1, N):
        # k=0のとき、スタートからゴールへ飛ぶしかない(得点0)ので、k=1から始める
        current_ans, k = 0, 1
        while k * c < N - 1:
            a = N - 1 - k * c
            b = a - c
            # k, cを決めたとき、進む距離<=戻る距離になる(負の座標に到達する)か、
            # 同じ座標に複数回到達する場合、得点を計算する意味がない
            if not (a <= b or b <= 0 or (a % c == 0 and a <= k * c)):
                current_ans += S[N - 1 - k * c] + S[k * c]
                ans = max(ans, current_ans)
            k += 1
    return ans
    # 参考: http://sigma1113.hatenablog.com/entry/2019/05/27/181729

N = int(input())
S = [int(i) for i in input().split()]
print(f_frog_jump(N, S))
