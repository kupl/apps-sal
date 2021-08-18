n = int(input())
f = [int(s) for s in str(input()).split()]


sortedF = [None] * n
for i in range(n):
    sortedF[f[i] - 1] = i


moves = 0
for i in range(n - 1):
    moves += abs(sortedF[i + 1] - sortedF[i])
print(moves)
