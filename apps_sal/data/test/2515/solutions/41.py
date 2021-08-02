n = 7**6; P = [0, 0] + [1] * n; S = [0] * n
for i in range(2, n):
    for j in range(2 * i, n, i): P[j] = 0
    S[i] += (P[i] == P[(i + 1) // 2] == 1) + S[i - 1]
for _ in "_" * int(input()): l, r = map(int, input().split()); print(S[r] - S[l - 1])
