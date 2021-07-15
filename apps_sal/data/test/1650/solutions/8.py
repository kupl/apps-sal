MOD = 10 ** 9 + 7
L = input()
N = len(L)
total = 0
one_count = 0
pow2, pow3 = [1], [1]
p2, p3 = 1, 1
for i in range(N):
    p2 = p2 * 2 % MOD
    p3 = p3 * 3 % MOD
    pow2.append(p2)
    pow3.append(p3)
for i in range(N):
    if L[i] == "1":
        total = (total + pow2[one_count] * pow3[N - i - 1]) % MOD
        one_count += 1
print(((total + pow2[one_count] * pow3[N - i - 1]) % MOD))

