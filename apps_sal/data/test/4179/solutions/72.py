(N, M, C) = map(int, input().split())
B = list(map(int, input().split()))
code_count = 0
answer = 0
while N > code_count:
    A = list(map(int, input().split()))
    sum = C
    for i in range(M):
        sum += A[i] * B[i]
    if sum > 0:
        answer += 1
    code_count += 1
print(answer)
