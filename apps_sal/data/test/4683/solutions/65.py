N = int(input())
A = list(map(int, input().split()))
mysum = sum(A)
total = 0
for i in range(N - 1):
    mysum -= A[i]
    total += A[i] * mysum
print(total % 1000000007)
