n = int(input())
K = [list(map(int, input().split())) for i in range(n)]
D1 = [0] * 2000
D2 = [0] * 2000
for i in range(len(K)):
    D1[K[i][0] - K[i][1] + 1000] += 1
    D2[K[i][0] - (1001 - K[i][1]) + 1000] += 1
P1 = 0
for e in D1:
    P1 += e * (e - 1) // 2
P2 = 0
for e in D2:
    P2 += e * (e - 1) // 2
print(P1 + P2)
