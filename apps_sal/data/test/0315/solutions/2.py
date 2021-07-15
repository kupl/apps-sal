n,k = map(int, input().split())
A = list(map(int, input().split()))
r = 0

for i in range(1,n):
    if A[i]+A[i-1] < k:
        r += k - A[i-1] - A[i]
        A[i] += k - A[i-1] - A[i]

print(r)
for i in range(n):
    print(A[i],end=" ")

