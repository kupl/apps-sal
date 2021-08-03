from math import floor, log2

N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

m = floor(log2(N))
print(sum(A[i // 2] for i in range(1, N)))
