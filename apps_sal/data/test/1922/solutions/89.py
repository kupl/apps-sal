(n, k) = map(int, input().split())
if n > 2 and k > 2:
    center = n * k - (k * 2 + (n - 2) * 2)
    print(center)
elif n == 1 and k == 1:
    print(1)
elif n == 1 or k == 1:
    if n > k:
        print(n - 2)
    else:
        print(k - 2)
else:
    print(0)
