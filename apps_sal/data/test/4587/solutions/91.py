import bisect
import itertools

N = int(input())  # それぞれのパーツの数
A = list(map(int, input().split()))  # 小さい
B = list(map(int, input().split()))  # 中くらい
C = list(map(int, input().split()))  # 大きい

# Cは並び替え不要
A.sort()
B.sort()

# Bの各要素でAを二分探索して返ってきたindexを先に保有しておく
b_counts = [0] * N
for i in range(N):
    b_count = bisect.bisect_left(A, B[i])
    b_counts[i] = b_count

cumsum_b_counts = list(itertools.accumulate(b_counts))
cumsum_b_counts = [0] + cumsum_b_counts

# Cの各要素でBを二分探索。上記で保有しておいたb_countsを活用する
total = 0
for c in C:
    count = bisect.bisect_left(B, c)
    total += cumsum_b_counts[count]

print(total)
