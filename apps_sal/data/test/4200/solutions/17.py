(N, M) = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort(reverse=True)
x = sum(A)
for i in range(M):
    if 4 * M * A[i] < x:
        print('No')
        break
else:
    print('Yes')
