N = int(input())
A = list(map(int, input().split()))

count = 0
for i in range(N):
    for k in range(A[i]):
        if A[i] % 2 == 0:
            A[i] /= 2
            count += 1
        else:
            break

print(count)
