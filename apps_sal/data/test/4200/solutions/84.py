(N, M) = map(int, input().split())
A = sorted(map(int, input().split()), reverse=True)
result = 'Yes'
for i in range(M):
    if A[i] / sum(A) < 1 / (4 * M):
        result = 'No'
        break
print(result)
