n = int(input())
M = [[c == 'C' for c in input()] for i in range(n)]
K = [sum(M[i]) for i in range(n)]
L = [sum(M[i][j] for i in range(n)) for j in range(n)]
ans = sum(k * (k - 1) // 2 for k in K) + sum(l * (l - 1) // 2 for l in L)
print(ans)
