# Input starts.
n = int(input())
f = [int(s) for s in str(input()).split()]

# print('n', n)
# print('f', f)

# Input ends.

# Solution starts.
sortedF = [None] * n
for i in range(n):
    sortedF[f[i] - 1] = i

# print('sortedF', sortedF)

moves = 0
for i in range(n - 1):
    moves += abs(sortedF[i + 1] - sortedF[i])
print(moves)

# print('moves', moves)

# Solution ends.
