N, K = list(map(int, input().split()))

d = [None] * K
sunuke = [0] * N
A = []
for i in range(K):
    d[i] = int(input())
    A.append(list(map(int, input().split())))

for members in A:
    for member in members:
        sunuke[member - 1] = 1

print((N - sum(sunuke)))
