n = int(input())
A = list(map(int, input().split()))
if n == 1:
    print(A[0])
elif n == 2:
    print(abs(A[0] - A[1]))
else:
    SUM = 0
    for i in range(n):
        SUM += abs(A[i])
    ANS = 0
    for i in range(n - 1):
        if ANS < SUM - abs(A[i]) - abs(A[i + 1]) + abs(A[i] - A[i + 1]):
            ANS = SUM - abs(A[i]) - abs(A[i + 1]) + abs(A[i] - A[i + 1])
    print(ANS)
