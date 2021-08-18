from numpy import ceil
N, D = map(int, input().split())
print(int(ceil(N / (2 * D + 1))))
