N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort(reverse=True)
sum_A = sum(A)

for i in range(M):
    if A[i] < sum_A / (4.0 * M):
        print('No')
        return

print('Yes')
