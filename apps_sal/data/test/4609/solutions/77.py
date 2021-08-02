N = int(input())
A = [int(input()) for c in range(N)]
A = sorted(A)

tmp = 1
cnt = 0
for i in range(N):
    if i + 1 < N:
        if A[i] == A[i + 1]:
            tmp += 1
        else:
            cnt += tmp % 2
            tmp = 1
    else:
        cnt += tmp % 2

print(cnt)
