n, k = list(map(int, input().split()))
l = (n + 1) >> 1
print(k + k - 1 if k <= l else (k - l) << 1)
