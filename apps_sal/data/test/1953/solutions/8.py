n = int(input())
serveTime = [int(x) for x in input().split()]
serveTime.sort()

answer = 0
curSum = 0
for i in range(len(serveTime)):
    if serveTime[i] >= curSum:
        curSum += serveTime[i]
        answer += 1

print(answer)

