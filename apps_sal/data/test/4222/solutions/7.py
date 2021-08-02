N, K = map(int, input().split())
D = []
A = []
for _ in range(K):
    D.append(int(input()))
    A.append(list(map(int, input().split())))

# 各人ごとに、持っているお菓子の個数を数え、個数0の人数を出力する
l = [0] * N
for i in range(K):
    for j in range(D[i]):
        l[A[i][j] - 1] += 1

print(l.count(0))
