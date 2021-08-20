(N, M, C) = map(int, input().split())
B = list(map(int, input().split()))
count = 0
for i in range(0, N):
    A = list(map(int, input().split()))
    answer = 0
    for j in range(0, M):
        answer += A[j] * B[j]
    answer += C
    if answer > 0:
        count += 1
print(count)
