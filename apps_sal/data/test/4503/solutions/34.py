(H, N) = map(int, input().split())
A = list(map(int, input().split()))
sum = 0
for i in range(len(A)):
    sum += A[i]
if H <= sum:
    print('Yes')
else:
    print('No')
