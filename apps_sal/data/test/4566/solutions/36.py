(N, M) = map(int, input().split())
nums = [0] * N
for i in range(M):
    (a, b) = map(int, input().split())
    nums[a - 1] += 1
    nums[b - 1] += 1
for ans in nums:
    print(ans)
