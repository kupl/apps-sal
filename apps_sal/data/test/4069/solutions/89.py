(x, k, d) = list(map(int, input().split()))
if abs(x) >= k * d:
    print(abs(x) - k * d)
elif abs(x) // d % 2 == k % 2:
    print(abs(x) % d)
else:
    print(d - abs(x) % d)
