N, M = [int(a) for a in input().split()]
A = []
B = []
for i in range(N):
    A.append(input())
for i in range(M):
    B.append(input())

wa = len(A[0])
wb = len(B[0])

matched = False
for i1 in range(N - M + 1):
    for j1 in range(wa - wb + 1):
        cnt = 0
        for i2 in range(M):
            if B[i2] == A[i1 + i2][j1:j1 + wb]:
                cnt += 1
        if cnt == M:
            matched = True
            break


if matched:
    print("Yes")
else:
    print("No")
