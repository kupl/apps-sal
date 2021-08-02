N, M, C = list(map(int, input().split()))
B = [int(i) for i in input().split()]

cnt = 0

for i in range(N):
    A = [int(i) for i in input().split()]
    sum = C
    for j in range(M):
        sum += A[j] * B[j]
        j += 1
    if sum > 0:
        cnt += 1
    i += 1

print(cnt)
