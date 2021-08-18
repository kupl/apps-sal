N, K, Q = map(int, input().split())
A = [int(i) for i in input().split()]

ans = float("inf")

for i in range(N):
    can = []

    left = 0
    while left < N:
        right = left
        while right < N and A[i] <= A[right]:
            right += 1

        L = right - left

        tmp = sorted([A[j] for j in range(left, right)])
        can += tmp[:max(0, L - K + 1)]

        left = right + 1

    can.sort()
    if len(can) >= Q:
        ans = min(ans, can[Q - 1] - A[i])

print(ans)
