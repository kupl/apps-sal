N, M, X = list(map(int, input().split()))
A = list(map(int, input().split()))
sum1 = 0
sum2 = 0
for i in range(M):
    if A[i] < X:
        sum1 += 1
    else:
        sum2 += 1
print((min(sum1, sum2)))
