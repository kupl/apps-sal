(X, Y) = list(map(int, input().split()))
for t in range(1, 100):
    if 2 ** (t - 1) * X <= Y:
        out = t
    else:
        break
print(out)
