N, X, Y = list(map(int, input().split()))

anss = [0] * N
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        d1 = j - i
        d2 = abs(i - X) + 1 + abs(Y - j)
        d = d1 if d1 <= d2 else d2
        anss[d] += 1

print(('\n'.join(map(str, anss[1:]))))
