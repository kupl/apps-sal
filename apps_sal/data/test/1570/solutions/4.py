(k, n, w) = list(map(int, input().split()))
s = w * (w + 1) // 2
print(max(0, s * k - n))
