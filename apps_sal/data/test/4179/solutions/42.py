(N, M, C) = map(int, input().split())
lists_B = list(map(int, input().split()))
lists_A = []
for _ in range(1, N + 1):
    lists_A.append(input().split())
SUM = 0
result = 0
for i in range(0, N):
    for j in range(0, M):
        SUM += int(lists_A[i][j]) * lists_B[j]
    if SUM + C > 0:
        result += 1
    SUM = 0
print(result)
