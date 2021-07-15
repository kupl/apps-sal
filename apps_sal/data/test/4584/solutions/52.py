n = int(input())

A = list(map(int, input().split()))

B = [0 for i in range(n)]
for i in range(n-1):
    B[A[i]-1] += 1
for i in range(n):
    print (B[i])
