S = input()
N = len(S)

ans = 2**(N - 1) * int(S[-1])
for i in range(1 << (N - 1)):
    res = 1
    for j in range(N - 1):
        if (i >> j) % 2 == 1:
            res *= 10
        else:
            res = 1
        ans += res * int(S[N - 2 - j])
print(ans)
