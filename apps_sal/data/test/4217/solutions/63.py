(N, M) = map(int, input().split())
l = [0] * M
for i in range(N):
    L = list(map(int, input().split()))
    num = L[0]
    A = L[1:]
    for j in range(num):
        l[A[j] - 1] += 1
print(l.count(N))
