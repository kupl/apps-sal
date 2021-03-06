from heapq import heappop, heapify
(N, K, *V) = list(map(int, open(0).read().split()))
ans = 0
for i in range(K + 1):
    for j in range(min(N + 1, i + 1)):
        for k in range(j + 1):
            right = N - j + k
            tmp = V[:k] + V[right:]
            put_out_cnt = i - j
            heapify(tmp)
            while tmp and put_out_cnt > 0:
                heappop(tmp)
                put_out_cnt -= 1
            ans = max(ans, sum(tmp))
print(ans)
