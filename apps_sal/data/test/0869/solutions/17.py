(a, b) = list(map(int, input().split()))
r1 = min(a, b)
r2 = (max(a, b) - min(a, b)) // 2
print(r1, r2)
