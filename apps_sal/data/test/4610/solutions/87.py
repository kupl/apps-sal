from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))
nums = [0] * N

for i in range(N):
    nums[A[i] - 1] += 1

nums.sort()

nums = deque(nums)

while True:
    if nums[0] == 0:
        nums.popleft()
    else:
        break
nums = list(nums)
if len(nums) <= K:
    print(0)
else:
    print(sum(nums[:len(nums) - K]))
