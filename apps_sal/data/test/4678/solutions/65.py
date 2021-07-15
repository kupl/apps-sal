N = int(input())
A = list(map(int, input().split()))

cnt = 0

for i in range(N-1):
    if A[i+1] >= A[i]:
        pass
    else:
        cnt += A[i] - A[i+1]
        A[i+1] = A[i]

print(cnt)
