N, K = list(map(int, input().split()))

a = K * (K + 1) // 2
if a > N:
    print("NO")
else:
    b = (N - a) // K
    c = N - a - b * K
    r = []
    for i in range(K):
        r.append(i + 1 + b + (1 if i + c >= K else 0))
    for i in range(K - 2):
        if r[i] * 2 < r[i + 1]:
            r[K - 1] += r[i + 1] - r[i] * 2
            r[i + 1] = r[i] * 2
    if r[K - 2] * 2 < r[K - 1]:
        print("NO")
    else:
        print("YES")
        print(' '.join(list(map(str, r))))
