K, N = map(int, input().split())
A = list(map(int, input().split()))

nums = [0] * N
for i in range(N - 1):
    nums[i] = A[i + 1] - A[i]
nums[-1] = K + A[0] - A[-1]

print(sum(nums) - max(nums))
return
