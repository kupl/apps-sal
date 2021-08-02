import heapq
n = int(input())
A = list(map(int, input().split()))
A_l = A[:n]
heapq.heapify(A_l)
A_l_sum = [sum(A_l)]
A_m = A[n:2 * n]
for i in range(n):
    p = A_m[i]
    heapq.heappush(A_l, p)
    q = heapq.heappop(A_l)
    A_l_sum.append(A_l_sum[-1] + p - q)
A_r = A[2 * n:3 * n]
for i in range(n):
    A_r[i] *= -1
for i in range(n):
    A_m[i] *= -1
A_m = A_m[::-1]
heapq.heapify(A_r)
A_r_sum = [sum(A_r)]
for i in range(n):
    p = A_m[i]
    heapq.heappush(A_r, p)
    q = heapq.heappop(A_r)
    A_r_sum.append(A_r_sum[-1] + p - q)
ans = -float("INF")
for i in range(n + 1):
    ans = max(ans, A_l_sum[i] + A_r_sum[-i - 1])
print(ans)
