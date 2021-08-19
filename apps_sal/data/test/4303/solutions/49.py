import bisect
(N, K) = list(map(int, input().split()))
X_list = list(map(int, input().split()))
INF = 10 ** 18
ans = INF
zero_index = bisect.bisect_left(X_list, 0)
candidate_list = []
ans = INF
for i in range(K + 1):
    head = zero_index - i
    tail = head + K - 1
    if head < 0 or tail > N - 1:
        continue
    if i == 0:
        ans = min(ans, abs(X_list[tail]))
    elif i == K:
        ans = min(ans, abs(X_list[head]))
    else:
        head_abs = abs(X_list[head])
        tail_abs = abs(X_list[tail])
        ans = min(ans, head_abs + tail_abs + min(head_abs, tail_abs))
print(ans)
