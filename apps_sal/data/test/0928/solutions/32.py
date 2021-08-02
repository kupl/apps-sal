import bisect
N, K = map(int, input().split())
A = [int(x) for x in input().split()]
left_sum = [0] * N  # 自分とそれより左側の要素の総和
now = 0
for h in range(N):
    now += A[h]
    left_sum[h] = now
ans = 0
for i in range(N):
    target = K + left_sum[i] - A[i]
    ans += N - bisect.bisect_left(left_sum, target)
print(ans)
