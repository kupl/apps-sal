(n, k) = list(map(int, input().split()))
A = list(map(int, input().split()))
B = [0] * n
Sum = 0
for i in range(len(A)):
    Sum += A[i]
    B[i] = Sum
Min = 100000000000.0
ind = 0
B = [0] + B
for i in range(1, n - k + 2):
    x = B[i + k - 1] - B[i - 1]
    if x < Min:
        Min = x
        ind = i
print(ind)
