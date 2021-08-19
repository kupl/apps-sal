N, K = map(int, input().split())
height = list(map(int, input().split()))

# N人で遊園地に遊びにいきました。
# ジェットコースターに乗るためには、身長が Kcm以上 必要です。
# 高橋君の仲間たちのうち、一番人気のジェットコースターに乗ることのできる人の数を出力してください。

availability = 0

for i in range(0, N):
    if height[i] >= K:
        availability += 1

print(availability)
