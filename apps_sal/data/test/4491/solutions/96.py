N = int(input())
A = [[],[]]
A[0] = list(map(int, input().split()))
A[1] = list(map(int, input().split()))
result = 0
for i in range(N+1):
    result = max(sum(A[0][:i]) + sum(A[1][i-1:]), result)
print(result)
