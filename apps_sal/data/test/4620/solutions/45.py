n = int(input())
C = []
S = []
F = []
for _ in range(n - 1):
    (c, s, f) = map(int, input().split())
    C.append(c)
    S.append(s)
    F.append(f)


def f(n, s, f):
    if n <= s:
        return s
    if n % f == 0:
        return n
    else:
        return n // f * f + f


for i in range(n - 1):
    now = S[i] + C[i]
    for j in range(i + 1, n - 1):
        now = f(now, S[j], F[j]) + C[j]
    print(now)
print(0)
