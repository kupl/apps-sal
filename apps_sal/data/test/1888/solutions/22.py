def R():
    return list(map(int, input().split()))


(n, m) = R()
p = [0] * n
for i in range(m):
    (a, b, c) = R()
    p[a - 1] -= c
    p[b - 1] += c
print(sum((i for i in p if i > 0)))
