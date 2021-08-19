(N, X) = (int(x) for x in input().split())
A = [int(x) for x in input().split()]
ret = 0
for i in range(N - 1):
    if A[i] + A[i + 1] > X:
        tmp = A[i] + A[i + 1] - X
        ret += tmp
        A[i + 1] -= min(A[i + 1], tmp)
print(ret)
