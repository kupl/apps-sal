N = int(input())
A = list(map(int, input().split()))

S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + A[i]

leftMiddle = 0
rightMiddle = 2

ans = float('inf')

for middle in range(2, N - 1):
    leftS = S[leftMiddle]
    rightS = S[middle] - leftS
    diff = abs(leftS - rightS)

    # 左側の更新
    for i in range(leftMiddle, middle):
        leftS += A[i]
        rightS -= A[i]
        if diff > abs(leftS - rightS):
            leftMiddle += 1
            diff = abs(leftS - rightS)
        else:
            break

    leftS = S[rightMiddle] - S[middle]
    rightS = S[-1] - S[rightMiddle]
    diff = abs(leftS - rightS)

    # 右側の更新
    for i in range(rightMiddle, N):
        leftS += A[i]
        rightS -= A[i]
        if diff > abs(leftS - rightS):
            rightMiddle += 1
            diff = abs(leftS - rightS)
        else:
            break

    B = S[leftMiddle]
    C = S[middle] - B
    D = S[rightMiddle] - S[middle]
    E = S[-1] - B - C - D

    diff = max(B, C, D, E) - min(B, C, D, E)
    ans = min(ans, diff)

print(ans)
