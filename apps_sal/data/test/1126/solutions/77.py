n, x, m = map(int, input().split())

ans = x
x0 = x
memo0 = [0] * (m + 1)
memo1 = [0] * (m + 1)
pair = [0, 0]

for i in range(1, n):
    x1 = (x0 % m * x0 % m) % m
    if memo0[x1] != 0:
        pair = [memo0[x1], i - 1]
        break
    else:
        memo0[x1] = i
        memo1[i] = memo1[i - 1] + x1
        x0 = x1
        pair = [0, i]

if pair[1] == n - 1:
    ans = memo1[pair[1]] + x
else:
    i, j = pair[0], pair[1]
    s0i = memo1[i - 1] + x
    sij = memo1[j] - memo1[i - 1]
    t0 = (n - i) // (j - i + 1)
    t1 = (n - i) % (j - i + 1)
    sje = memo1[t1 + i - 1] - memo1[i - 1]
    ans = s0i + sij * t0 + sje

print(ans)
