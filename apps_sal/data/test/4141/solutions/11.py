# 155_b
N = int(input())
A = input().split()
result = ''
for i in range(N):
    A[i] = int(A[i])
    if A[i] % 2 == 0:
        if A[i] % 3 != 0 and A[i] % 5 != 0:
            result = 'DENIED'
            break
    else:
        result = 'APPROVED'
print(result)
