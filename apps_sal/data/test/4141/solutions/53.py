N = int(input())
A = list(map(int, input().split()))

gusu = 0
cnt = 0
for i in range(N):
    if A[i] % 2 == 0:
        gusu += 1

        if A[i] % 3 == 0 or A[i] % 5 == 0:
            cnt += 1

if gusu == cnt:
    print('APPROVED')
else:
    print('DENIED')
