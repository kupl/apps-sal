N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

l = [0] * M
for i in range(N):
    num = A[i][0]
    for j in range(num):
        l[A[i][j + 1] - 1] += 1

print(l.count(N))
