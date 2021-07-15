from collections import defaultdict
N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
A = [(A[i], 1) for i in range(N)]

changes = [None] * M
for i in range(M):
    b, c = list(map(int, input().split()))
    changes[i] = (c, b)

allVals = A + changes

allVals.sort(key = lambda x:x[0], reverse = True)
# print(allVals)

i = 0
j = -1
res = 0
while True:
    j += 1
    res += allVals[j][0] * allVals[j][1]
    i += allVals[j][1]

    if i >= N:
        res -= allVals[j][0] * (i - N)
        break



print(res)

