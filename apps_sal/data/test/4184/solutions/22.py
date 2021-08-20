N = int(input())
W = list(map(int, input().split()))
S1 = 0
S2 = 0
zettai = []
for i in range(N - 1):
    S1 += W[i]
    for j in range(i + 1, N):
        S2 += W[j]
    zettai.append(abs(S2 - S1))
    S2 = 0
print(min(zettai))
