N = int(input())
A = list(map(int, input().split()))
A = sorted(A, reverse=True)
L = []
cnt = 0
i = 0
while i <= N - 2:
    if A[i] == A[i + 1]:
        L.append(A[i])
        i += 1
        cnt += 1
        if cnt == 2:
            break
    i += 1
if len(L) == 2:
    print(L[0] * L[1])
else:
    print(0)
