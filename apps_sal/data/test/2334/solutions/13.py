import bisect
import math
n = int(input())
vallet = []
vallet = list(map(int, input().strip().split()))
maxst, fee = list(map(int, input().strip().split()))
vallet.sort()
index = bisect.bisect(vallet, maxst)

numsplit = 0
for i in range(index, len(vallet)):
    numsplit += math.ceil(float(vallet[i] - maxst) / (maxst + fee))

print(numsplit * fee)
