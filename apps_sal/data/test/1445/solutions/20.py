n = int(input())
A = list(map(int, input().split()))
for i in range(n//2):
    if i % 2 == 0:
        A[i], A[n-i-1] = A[n-i-1], A[i]
for i in A:
    print(i, sep = '', end = ' ')

