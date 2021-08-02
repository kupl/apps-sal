n, m = map(int, input().split())
A = [n // 5, n // 5, n // 5, n // 5, n // 5]
B = [m // 5, m // 5, m // 5, m // 5, m // 5]

for i in range(n % 5):
    A[i] += 1
for i in range(m % 5):
    B[i] += 1
print(A[0] * B[3] + A[3] * B[0] + A[1] * B[2] + A[2] * B[1] + A[4] * B[4])
