n = int(input())
(C, S, F) = ([], [], [])
for i in range(n - 1):
    (c, s, f) = map(int, input().split())
    C.append(c)
    S.append(s)
    F.append(f)
for i in range(n - 1):
    t = 0
    for j in range(i, n - 1):
        if S[j] > t:
            t = S[j]
        if (t - S[j]) % F[j] == 0:
            t += C[j]
        else:
            t += F[j] - (t - S[j]) % F[j] + C[j]
        if j == n - 2:
            print(t)
print(0)
