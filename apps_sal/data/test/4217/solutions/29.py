n, m = list(map(int, input().split()))
nums = [0 for num in range(m)] 
for i in range(n):
    k = [int(s) for s in input().split()]
    for j in range(1, len(k)):
        nums[k[j] - 1] += 1
print((nums.count(n)))

