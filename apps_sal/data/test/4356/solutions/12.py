N, M = list(map(int, input().split()))
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]
R = list(range(N-M+1))

for i in R:
    for j in R:
        for k in range(M):
            if A[j+k][i:i+M] != B[k]:
                break
        else:
            print('Yes')
            return
print('No')

