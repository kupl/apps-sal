# N時間駐車した時の最小料金を求める

N, A, B = list(map(int, input().split()))

fee = [N * A, B]
print((min(fee)))
