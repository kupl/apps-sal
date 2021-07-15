n = int(input())
M = []
S = set()
L = list(map(int, input().split()))
for i in range(n - 1, -1, -1):
    if L[i] not in S:
        S.add(L[i])
        M.append(L[i])
print(len(M))
M.reverse()
print(*M)
