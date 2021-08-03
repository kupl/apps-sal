H, N = map(int, input().split())
A = list(map(int, input().split()))
sum = 0
for i in range(N):
    sum += A[i]
if sum >= H:
    print('Yes')
else:
    print('No')
