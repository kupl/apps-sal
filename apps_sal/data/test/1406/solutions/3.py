def In():
    return list(map(int, input().split()))


(n, k, d) = In()
if n > k ** d:
    print(-1)
else:
    k1 = 1
    for i in range(d):
        print(' '.join(map(str, [j // k1 % k + 1 for j in range(n)])))
        k1 = k1 * k
