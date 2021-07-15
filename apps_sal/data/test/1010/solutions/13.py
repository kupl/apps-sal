n, a, v = int(input()), list(map(int, input().split())), 1
p = [i for i, ai in enumerate(a) if ai]
for i in range(1, len(p)):
    v *= p[i] - p[i - 1]
print(v if p else 0)
