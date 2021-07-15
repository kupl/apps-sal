


inp  = input().split(' ')
n = int(inp[0])
k = int(inp[1])

nums = input().split(' ')
nums = [int(x) for x in nums]
sums = [0]
for x in nums:
  sums += [x + sums[-1]]

m = 0
for i in range(0, n-k+1):
  m = max(m, sums[i+k] - sums[i])
print(((m+k)/2))






