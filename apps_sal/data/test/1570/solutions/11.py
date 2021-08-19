(k, n, w) = map(int, input().split())
sum1 = k * (w * (w + 1)) // 2
print(max(0, sum1 - n))
