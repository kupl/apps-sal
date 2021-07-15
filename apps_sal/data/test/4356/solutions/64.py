N, M = list(map(int, input().split()))
A = []
for _ in range(N):
    a = input()
    A.append(a)

B = []
for _ in range(M):
    b = input()
    B.append(b)

idx = [0, 0]
while True:
    if idx[0] == N - 1 and idx[1] == N - 1:
        break
    if A[idx[0]][idx[1]] == B[0][0]:
        check = False
        for i in range(M):
            for j in range(M):
                if 0 <= idx[0] + i < N and 0 <= idx[1] + j < N:
                    if A[idx[0] + i][idx[1] + j] != B[i][j]:
                        check = True
                        break
                else:
                    check = True
                    break
            if check:
                break

        if not check:
            print('Yes')
            return
    if idx[1] < N - 1:
        idx[1] += 1
        continue
    else:
        idx[0] += 1
        idx[1] = 1
        continue

if A[-1][-1] == B[0][0] and M == 1:
    print('Yes')
    return

print('No')

