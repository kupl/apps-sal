N = int(input())
A = list(map(int, input().split()))
A.sort()
A.append(10**12)
MAX = A[N - 1]
ans = N
for i in range(N):
    if abs(A[i] - MAX / 2) < abs(A[ans] - MAX / 2):
        ans = i
print(MAX, A[ans])
