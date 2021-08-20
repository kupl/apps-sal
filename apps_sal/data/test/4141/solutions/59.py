N = int(input())
A = list(map(int, input().split()))
t = 'APPROVED'
for i in range(len(A)):
    if A[i] % 2 == 0:
        if A[i] % 3 == 0 or A[i] % 5 == 0:
            continue
        else:
            t = 'DENIED'
print(t)
