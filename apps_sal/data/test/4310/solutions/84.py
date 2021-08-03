A = list(map(int, input().split()))
A = sorted(A)
ret = 0
for i in range(len(A) - 1):
    ret += abs(A[i] - A[i + 1])

print(ret)
