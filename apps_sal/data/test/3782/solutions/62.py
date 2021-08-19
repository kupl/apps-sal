# 解説AC
N, K, Q = map(int, input().split())
A = [int(i) for i in input().split()]

ans = float("inf")

# A[i]: 最小値X
for i in range(N):
    # 最大値Yの候補
    can = []

    # A[left:right]: A[i]以上の連続部分列
    left = 0
    while left < N:
        right = left
        while right < N and A[i] <= A[right]:
            right += 1

        # 連続部分列長
        L = right - left

        tmp = sorted([A[j] for j in range(left, right)])
        can += tmp[:max(0, L - K + 1)]

        left = right + 1

    # Q番目に小さいものがYの最小値
    can.sort()
    if len(can) >= Q:
        ans = min(ans, can[Q - 1] - A[i])

print(ans)
