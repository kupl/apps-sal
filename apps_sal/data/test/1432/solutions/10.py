N = int(input())
A = list(map(int, input().split()))

x = [-1] * N

s = sum(A)
temp = 0
for i in range(2, N, 2):
    temp += A[i - 1]
x[0] = s - 2 * temp

for i in range(1, N):
    x[i] = 2 * A[i - 1] - x[i - 1]
print((*x))
