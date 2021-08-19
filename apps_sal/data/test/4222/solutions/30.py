N, K = map(int, input().split())
D = []
A = []
for _ in range(K):
    D.append(int(input()))
    A.append(list(map(int, input().split())))

# お菓子を持っている人を数える。すると持っていない人間は、Nから持っている人の数を引いたもの
l = [0] * N
for i in range(K):
    for j in range(D[i]):
        l[A[i][j] - 1] = 1

print(N - sum(l))
