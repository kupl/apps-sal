(x, k, d) = list(map(int, input().split()))
if abs(x) // d >= k:
    print(abs(x) - d * k)
elif (k - abs(x) // d) % 2 == 0:
    print(abs(x) % d)
else:
    print(d - abs(x) % d)
