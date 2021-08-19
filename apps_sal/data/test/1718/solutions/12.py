# 問題制約見間違えて1~Nの任意の数字をとると勘違いして作ったコード(一応通る)
# 4 2
# 1 2 1 2
# ↑のケースは存在しないパターンだが、所謂解答例の場合3となるがこのコードだと2となる
N, K = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
correction_value = 0
for i in range(0, N, K - 1):
    cnt += 1
    if i + correction_value + K >= N:
        break
    else:
        for j in range(1, K):
            arr[j] = min(arr[j], arr[j - 1])
        if arr[i + correction_value + K] == arr[i + correction_value + K - 1]:
            correction_value += 1
print(cnt)
