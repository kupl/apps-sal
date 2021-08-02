n = int(input().strip())
p = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
moves = 1
for i in range(1, n):
    if c[p[i - 1] - 1] != c[i]:
        moves += 1
print(moves)
