N = int(input())
A = [int(x) for x in input().split()]
from statistics import mean
from math import floor, ceil
meanA = mean(A)
if meanA < floor(meanA) + 0.5:
    meanA = floor(meanA)
else:
    meanA = ceil(meanA)
ans = 0
for a in A:
    ans += (a-meanA)**2
print(ans)
