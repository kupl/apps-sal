P = 998244353
N = int(input())
i2 = pow(2, P - 2, P)
iv = pow(i2, N - 1, P)
s = 0
t = 1
ANS = [i2 * N % P] * (1 if N <= 2 else 2)
for i in range(2, (N + 1) // 2):
    a = (i * 2 - 1) * t % P
    s = (s + a) % P
    ANS.append((i2 * N + s * iv) % P)
    t = t * 4 % P
for i in range(N // 2):
    ANS.append(ANS[N // 2 - i - 1])
print("\n".join(map(str, ANS)))
