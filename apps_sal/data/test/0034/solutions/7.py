(n, a, b) = [int(v) for v in input().split()]
best = 0
for k in range(1, n):
    fst = k
    snd = n - k
    best = max(best, min(a // fst, b // snd))
print(best)
