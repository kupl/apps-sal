N, X, M = list(map(int, input().split()))

r = [-1 for _ in range(M)]
a = X
r[a] = 0
p = [a]

# M回繰り返せば，必ずかぶる
for i in range(1, M + 1):
    an = a ** 2 % M
    if r[an] >= 0:
        break
    r[an] = i
    p.append(an)
    a = an

q = p[r[an] :]
p = p[: r[an]]

if N <= len(p):
    ans = sum(p[:N])
else:
    ans = sum(p)
    N -= len(p)
    a, b = divmod(N, len(q))
    ans += a * sum(q)
    ans += sum(q[:b])

print(ans)

