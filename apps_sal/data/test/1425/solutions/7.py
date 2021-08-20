n = int(input())
A = [int(x) for x in input().split()]
A.sort()
B = [-1] * n
j = 0
for i in range(n):
    B[j] = A[i]
    if j <= 0:
        j = -j + 1
    else:
        j *= -1
ok = True
for i in range(n):
    if B[i - 1] >= B[i - 2] + B[i]:
        ok = False
if ok:
    print('YES')
    print(*B)
else:
    print('NO')
