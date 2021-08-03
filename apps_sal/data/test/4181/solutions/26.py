N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
count = 0
tmp = 0
for i in range(N):
    tmp = min(A[i], B[i])
    count += tmp
    tmp = min(A[i + 1], B[i] - tmp)
    A[i + 1] -= tmp
    count += tmp
print(count)
