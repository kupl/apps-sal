(n, k) = list(map(int, input().split()))
s = input()
W = [[0, 1, 0], [1, 1, 2], [0, 2, 2]]
B = [[0] * n for _ in range(2)]
J = 'RPS'
for j in range(n):
    B[0][j] = 0 if s[j] == 'R' else 1 if s[j] == 'P' else 2
for i in range(k):
    for j in range(n):
        B[-~i % 2][j] = W[B[i % 2][j]][B[i % 2][(j + 2 ** i) % n]]
print(J[B[k % 2][0]])
