N = int(input())
A = list(map(int, input().split()))
flag = True
A = sorted(A)
for i in range(N - 1):
    if A[i] == A[i + 1]:
        flag = False
if flag:
    print('YES')
else:
    print('NO')
