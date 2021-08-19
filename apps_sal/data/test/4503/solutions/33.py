(H, N) = map(int, input().split())
A = [int(i) for i in input().split()]
for i in range(N):
    H -= A[i]
if H <= 0:
    print('Yes')
else:
    print('No')
