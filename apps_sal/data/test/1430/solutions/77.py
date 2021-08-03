n, k = map(int, input().split())
S = list(map(int, list(input())))
# 尺取り法.
# 右側の初期化.//これを不規則に動かす.
ridx = 1
# パラメータの初期化.//これでridxを制御する.
# 最初が0だった場合、最初から反転が必要.
cnt = 0 if S[0] == 1 else 1
# 答えの初期化.//この最大を探す.
ans = 0
# 左側を0からn-1まで動かしていく.
for lidx in range(n):
    # 現在地が1で一つ前が0だった場合、カウントを減らす.
    if lidx > 0 and S[lidx] == 1 and S[lidx - 1] == 0:
        cnt -= 1
    # 右端がn未満なら右に一つずつ動かしていく.
    while ridx < n:
        # もし現在地が0で、一つ前が1なら
        if S[ridx] == 0 and S[ridx - 1] == 1:
            # カウントがk未満ならカウントを増やし、そうでないならループを脱する.
            if cnt < k:
                cnt += 1
            else:
                break
        ridx += 1
    ans = max(ans, ridx - lidx)
print(ans)
