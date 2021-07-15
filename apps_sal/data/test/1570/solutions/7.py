k, n, w = list(map(int, input().split()))
print(max(0, k * (w * (w + 1) // 2) - n))

