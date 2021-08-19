N, M, C = map(int, input().split())
B = list(map(int, input().split()))

# N個のソースコードのうち、この問題に正答するソースコードの個数を出力

count = 0

for N in range(N):
    A = list(map(int, input().split()))
    culc = list()
    culc.append(C)

    for i in range(M):
        d = B[i] * A[i]
        culc.append(d)

    if sum(culc) > 0:
        count += 1

print(count)
