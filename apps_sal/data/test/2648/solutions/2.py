from math import ceil
N = int(input())
A = list(map(int, input().split()))
M = len(set(A))
print(N - ceil((N - M) / 2) * 2)
