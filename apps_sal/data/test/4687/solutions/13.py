n, k, *x = list(map(int, open(0).read().split()))
for a, b in sorted(zip(x[0::2], x[1::2])):
    k -= b
    if k < 1:
        print(a)
        break
