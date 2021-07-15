n, k, d = list(map(int, input().split()))
if k < n ** (1 / d):
    print(-1)
else:
    k1 = 1
    for i in range(d):
        print(" ".join(map(str, [(j // k1 % k) + 1 for j in range(n)])))
        k1 = k * k1

