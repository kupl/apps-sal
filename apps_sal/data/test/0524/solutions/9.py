import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
n = int(input())
arry = list(map(int, input().split()))
maxNum = max(arry)
maxRecur = maxNum ** (1 / (n - 1))
currMin = float('inf')
arry.sort()
for i in range(int(maxRecur) + 2):
    curr = 0
    for j in range(n):
        curr += abs(i ** j - arry[j])
    currMin = min(currMin, curr)
print(currMin)
