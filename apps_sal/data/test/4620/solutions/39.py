N = int(input())
lis = [[0, 0, 1]]
for i in range(N - 1):
    C, S, F = list(map(int, input().split()))
    lis.append([C, S, F])

for i in range(N):
    C, S_ij, F = 0, 0, 1
    for j in range(i + 1, N):
        C, S, F = lis[j]
        S = max(S, S_ij)
        S_ij = C + ((S - 1) // F + 1) * F
    print(S_ij)
