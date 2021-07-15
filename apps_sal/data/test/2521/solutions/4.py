import heapq

N = int(input())
A = list(map(int, input().split()))

leftQue = []
rightQue = []

leftSum = 0
rightSum = 0

for i in range(N):
    heapq.heappush(leftQue, A[i])
    leftSum += A[i]

    heapq.heappush(rightQue, -A[-1 - i])
    rightSum -= A[-1 - i]

left = [-float('inf') for _ in range(3 * N)]
right = [-float('inf') for _ in range(3 * N)]

left[N - 1] = leftSum

for middle in range(N, 2 * N):
    leftSum += A[middle]
    leftSum -= heapq.heappushpop(leftQue, A[middle])
    left[middle] = leftSum

right[2 * N - 1] = rightSum
for middle in range(2 * N - 1, N - 1, -1):
    rightSum -= A[middle]
    rightSum -= heapq.heappushpop(rightQue, -A[middle])
    right[middle - 1] = rightSum

ans = -float('inf')
for l, r in zip(left, right):
    ans = max(ans, l + r)

print(ans)
