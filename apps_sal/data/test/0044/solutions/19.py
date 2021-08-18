
d, k, a, b, t = [int(x) for x in input().split()]

if d <= k:
    print(d * a)
else:
    left = 0
    right = (d // k) + 1
    if k * b - k * a - t > 0:
        left = (d * (b - a) - ((d // k) + 1) * t) / (k * b - k * a - t)
    elif k * b - k * a - t < 0:
        right = (d * (b - a) - ((d // k) + 1) * t) / (k * b - k * a - t)
    N = int(right)
    M = int(left) + 1
    if M >= N:
        print(d * a + (d // k) * t)
    else:
        if not N < right:
            N = N - 1
        if N > left and M < right:
            A = (N - 1) * t + N * k * a + (d - N * k) * b
            B = (M - 1) * t + M * k * a + (d - M * k) * b
            print(min(A, B))
        else:
            if N > left:
                print((N - 1) * t + N * k * a + (d - N * k) * b)
            if M < right:
                print((M - 1) * t + M * k * a + (d - M * k) * b)
