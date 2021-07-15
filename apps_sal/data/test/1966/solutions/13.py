n = int(input())
brd = []
for i in range(4):
    brd.append([list(map(int, list(input()))) for _ in range(n)])
    if i < 3:
        _ = input()

ans = 4 * n**2
for i in range(16):
    if sum([(i >> j) & 1 for j in range(4)]) != 2:
        continue
    ans = min(ans, sum([abs((r + c + ((i >> j) & 1)) % 2 - brd[j][r][c]) \
                    for j in range(4) for r in range(n) for c in range(n)]))

print(ans)

