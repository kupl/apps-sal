(N, K) = map(int, input().split())
A = list(map(int, input().split()))
B = [0 for i in range(N + 1)]
for a in A:
    B[a] += 1
nums = [b for b in B if b > 0]
nums.sort()
n = len(nums)
if n <= K:
    print(0)
else:
    print(sum(nums[:n - K]))
