import heapq

_, m, k = list(map(int, input().split()))
a, b = heapq.nlargest(2, list(map(int, input().split())))
print(a * m - m // (k + 1) * (a - b))

