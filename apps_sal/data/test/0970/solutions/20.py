n = int(input())
p = sorted([int(x) for x in input().split()])

moves_B = sum([abs(2 * i + 1 - p[i]) for i in range(n // 2)])
moves_W = sum([abs(2 * i + 2 - p[i]) for i in range(n // 2)])

print(min(moves_B, moves_W))
