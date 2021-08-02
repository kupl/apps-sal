N = int(input())
A = list(map(int, input().split()))
ok = True
for i in range(N):
    for j in range(N - i - 1):
        if abs(A[j] - A[j + 1]) > 1:
            ok = False
    idx = A.index(max(A))
    A = A[:idx] + A[idx + 1:]
if ok:
    print('YES')
else:
    print('NO')
