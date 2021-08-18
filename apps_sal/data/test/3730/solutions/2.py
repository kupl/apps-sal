import sys
sequenceLength = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
ans = 0
leftList = [1] * sequenceLength
rightlist = [1] * sequenceLength
for i in range(1, sequenceLength):
    if sequence[i - 1] < sequence[i]:
        leftList[i] += leftList[i - 1]
    ans = max(ans, leftList[i])

if ans < sequenceLength:
    ans += 1

for i in range(sequenceLength - 2, 0, -1):
    if sequence[i + 1] > sequence[i]:
        rightlist[i] += rightlist[i + 1]

for i in range(1, sequenceLength - 1):
    if sequence[i + 1] - sequence[i - 1] >= 2:
        ans = max(ans, leftList[i - 1] + 1 + rightlist[i + 1])

print(ans)
