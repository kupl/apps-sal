import sys

def findmax2(nums, n):
    inter = {}
    inter[0] = 0
    inter[1] = nums.get(1, 0)
    for i in range(2, n + 1):
        inter[i] = max(inter[i-2] + nums.get(i, 0), inter[i-1])

    return inter[n]
    
count = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

pnums = {}



for n in nums:
    pnums[n] = pnums.get(n, 0) + n



print(findmax2(pnums, max(nums)))
