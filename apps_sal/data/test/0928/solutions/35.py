import bisect
(N, K) = list(map(int, input().split()))
A_list = list(map(int, input().split()))
A_ruisekiwa = [0] * (N + 1)
for i in range(1, N + 1):
    A_ruisekiwa[i] = A_ruisekiwa[i - 1] + A_list[i - 1]
ans = 0
for i in range(N):
    a = K + A_ruisekiwa[i]
    t_i = bisect.bisect_left(A_ruisekiwa, a)
    if t_i <= N:
        ans += N - t_i + 1
print(ans)
