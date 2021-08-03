from math import ceil
N = int(input())
A = [0] * 5
for i in range(5):
    A[i] = int(input())
ans = ceil(N / min(A)) + 4
print(ans)
