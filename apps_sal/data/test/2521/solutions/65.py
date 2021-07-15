import heapq
N = int(input())
A = list(map(int,input().split()))
left = [sum(A[:N])]
h1 = A[:N]
heapq.heapify(h1)
for i in range(N):
    heapq.heappush(h1, A[N+i])
    temp = heapq.heappop(h1)
    left.append(left[-1] + A[N+i] - temp)
right = [sum(A[2*N:])]
h2 = list(map(lambda x: -x, A[2*N:]))
heapq.heapify(h2)
for i in range(N):
    heapq.heappush(h2, -A[2*N-1-i])
    temp = -1 * heapq.heappop(h2)
    right.append(right[-1] + A[2*N-1-i] - temp)
ans = float('-inf')
for i in range(N+1):
    ans = max(ans, left[i] - right[-(i+1)])
print(ans)
