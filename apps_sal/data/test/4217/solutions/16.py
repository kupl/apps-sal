N, M = map(int, input().split())

l = [0] * M
for _ in range(N):
    A = list(map(int, input().split()))
    for j in range(A[0]):
        l[A[j + 1] - 1] += 1

# lの要素でNである個数を出力
print(l.count(N))
