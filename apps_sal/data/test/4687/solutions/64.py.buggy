N, K, *L = [int(a)for a in open(0).read().split()]
for a, b in sorted(zip(L[::2], L[1::2])):
    K -= b
    if K < 1:
        print(a)
        return
