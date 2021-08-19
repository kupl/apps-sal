(n, k) = map(int, input().split())
nums = list(map(int, input().split()))
suffixSum = [nums[-1]]
for i in nums[-2::-1]:
    suffixSum.append(suffixSum[-1] + i)
suffixSum = suffixSum[:-1]
suffixSum.sort(reverse=True)
ans = sum(nums)
ans += sum(suffixSum[:k - 1])
print(ans)
