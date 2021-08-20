n = int(input())
xs = list(map(int, input().split()))
u = sum(xs) // n
moves = 0
for i in range(n - 1):
    moves += abs(u - xs[i])
    xs[i + 1] += xs[i] - u
print(moves)
