N, M = map(int, input().split())
A = [input() for i in range(N)]
B = [input() for i in range(M)]
for i in range(N - M + 1):
    pos = -1
    for j in range(A[i].count(B[0])):
        pos = A[i].find(B[0], pos + 1)
        for k in range(1, M):
            if A[i + k].find(B[k], pos) != pos:
                break
        else:
            print('Yes')
            break
    else:
        continue
    break
else:
    print('No')
