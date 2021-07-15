N = int(input())
A = list(map(int, input().split()))

lis = [0] * N
for i in range(N - 1):
    lis[(A[i] - 1)] += 1

for i in range(N):
    print((lis[i]))

