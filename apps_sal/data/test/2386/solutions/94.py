N = int(input())
A = list(map(int, (input().split())))
suma = 0
sumabs = 0
for i in range(N):
    A[i] -= i + 1
    suma += A[i]
A.sort()
b = (A[N // 2] + A[(N - 1) // 2]) // 2
ans = 0
for i in range(N):
    ans += abs(A[i] - b)
print(ans)
