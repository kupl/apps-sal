n = int(input())
A = list(map(int, input().split()))
isOk = True
for i in range(n):
    if A[i] % 2 != 0:
        continue
    if A[i] % 3 != 0 and A[i] % 5 != 0:
        isOk = False
if isOk:
    print('APPROVED')
else:
    print('DENIED')
