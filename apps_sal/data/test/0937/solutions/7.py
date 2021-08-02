n, k = map(int, input().split())
A = list(map(int, input().split()))
T = list(map(int, input().split()))

gain = [0] * (n - k + 1)
for i in range(k):
    if T[i] == 0:
        gain[0] += A[i]

for i in range(1, n - k + 1):
    gain[i] = gain[i - 1]
    if T[i - 1] == 0:
        gain[i] -= A[i - 1]
    if T[i + k - 1] == 0:
        gain[i] += A[i + k - 1]

sum = 0
for i in range(n):
    if T[i] == 1:
        sum += A[i]

print(sum + max(gain))
