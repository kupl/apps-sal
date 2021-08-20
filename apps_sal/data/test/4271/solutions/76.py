N = int(input())
A = list(map(int, input().split()))
A = list([x - 1 for x in A])
B = list(map(int, input().split()))
C = list(map(int, input().split()))
cnt = 0
for i in range(N):
    cnt += B[A[i]]
    if A[i] == A[i - 1] + 1 and i != 0:
        cnt += C[A[i - 1]]
print(cnt)
