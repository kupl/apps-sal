import heapq
N = int(input())
A = list(map(int, input().split()))
left = A[:N]
left_total = [sum(left)]
heapq.heapify(left)
for i in range(N, 2 * N):
    l = heapq.heappop(left)
    if l < A[i]:
        heapq.heappush(left, A[i])
        left_total.append(left_total[-1] - l + A[i])
    else:
        heapq.heappush(left, l)
        left_total.append(left_total[-1])
right = [-i for i in A[2 * N:]]
right_total = [sum(right)]
heapq.heapify(right)
for i in reversed(range(N, 2 * N)):
    r = heapq.heappop(right)
    if r < -A[i]:
        heapq.heappush(right, -A[i])
        right_total.append(right_total[-1] - r - A[i])
    else:
        heapq.heappush(right, r)
        right_total.append(right_total[-1])
right_total = right_total[::-1]
ans = -float('inf')
for i in range(len(left_total)):
    ans = max(ans, left_total[i] + right_total[i])
print(ans)
