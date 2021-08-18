N = int(input())
A = list(map(int, input().split()))
A.sort()
minNum = A[0]
maxNum = A[N - 1]
countList = [0] * (10**6 + 1)
answer = 0

for i in A:
    countList[i] += 1

for j in range(minNum, maxNum + 1):
    if countList[j] > 0:
        for k in range(2 * j, 10**6 + 1, j):
            countList[k] = 0
    if countList[j] == 1:
        answer += 1

print(answer)
