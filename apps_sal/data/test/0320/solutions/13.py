n = int(input())
count = -1
A = [0] * 3
for i in range(n):
    a, b = list(map(int, input().split()))
    if a % 2 == 1 and b % 2 == 1:
        A[0] += 1
    elif a % 2 == 1:
        A[1] += 1
    elif b % 2 == 1:
        A[2] += 1
if A[0] % 2 == 0 and (A[1] + A[2]) % 2 == 0:
    print(A[1] % 2)
elif (A[1] + A[2]) % 2 == 0 and (A[1] + A[2]) >= 2:
    if A[1] % 2 == A[2] % 2 == 1:
        print(0)
    else:
        print(1)
else:
    print(-1)
