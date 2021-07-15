N, M = list(map(int, input().split()))
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]
flag = 0
for i in range(N-M+1):
    for j in range(N-M+1):
        if [line[j:j+M] for line in A[i:i+M]] == B:
            flag = 1
print(('Yes' if flag == 1 else 'No'))


