N = int(input())
A = list(map(int, input().split()))
l = 0
while True:
    A = sorted(A)
    m = A[l]
    for i in range(l + 1, N):
        A[i] %= m
    l = A.count(0)
    if l == N - 1:
        break
A = sorted(A)
print(A[-1])
