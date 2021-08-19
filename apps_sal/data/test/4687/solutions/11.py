(N, K, *l) = map(int, open(0).read().split())
for (a, b) in sorted(zip(l[::2], l[1::2])):
    if (K := (K - b)) <= 0:
        break
print(a)
