(n, m, k) = list(map(int, input().split()))
p = list(map(int, input().split()))
(deleted, right) = (0, 0)
c = 0
moves = 0
while c < m:
    right = (1 + (p[c] - deleted - 1) // k) * k + deleted
    while c < len(p) and p[c] <= right:
        c += 1
        deleted += 1
    moves += 1
print(moves)
