# 先頭の最大と最後尾の最小を求める
card_num, gate_num = map(int, input().split())
lmax, rmin = map(int, input().split())  # 最初の入力がlの最大とrの最小
for i in range(1, gate_num):
    l, r = map(int, input().split())
    lmax = max(lmax, l)  # lmaxにlmaxとlの大きい方
    rmin = min(rmin, r)  # rminにrminとrの小さい方
print(max(0, rmin - lmax + 1))  # 0かrmin-lmax+1の大きい方を出力
