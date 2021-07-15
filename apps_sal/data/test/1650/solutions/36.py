MOD = 10 ** 9 + 7
L = input()
N = len(L)
p3 = [1] * N
for i in range(1, N):
    p3[i] = p3[i - 1] * 3 % MOD
p2 = 1
total = 0
for i in range(N):
    if L[i] == "1":
        total = (total + p2 * p3[N - i - 1]) % MOD
        p2 = p2 * 2 % MOD
print((total + p2 * p3[N - i - 1]) % MOD)
