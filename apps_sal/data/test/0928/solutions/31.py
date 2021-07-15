N, K = list(map(int, input().split()))
A = [int(x) for x in input().split()]

# しゃくとり法の基本問題
left = 0
right = 0
# おそらくインデックスの範囲の取り扱いで間違える
count = 0
total = 0
while left < N and right < N:
    total += A[right]
    while total >= K:
        count += N - right
        total -= A[left]
        left += 1
    right += 1
print(count)

