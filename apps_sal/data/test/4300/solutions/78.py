N = int(input())
d = list(map(int, input().split()))
kaifuku = 0
for i in range(N):
    for j in range(i + 1, N):
        kaifuku += d[i] * d[j]
print(kaifuku)
