n = int(input())
A = list(map(int, input().split()))
A.sort()
success = True
for i in range(n - 1):
    if A[i] == A[i + 1]:
        success = False
        break
if success:
    print('YES')
else:
    print('NO')
