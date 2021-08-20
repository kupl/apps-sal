n = int(input())
b = [input() for _ in range(n)]
ans = True
for i in range(n):
    for j in range(n):
        ans &= len([1 for (di, dj) in [(1, 0), (-1, 0), (0, 1), (0, -1)] if 0 <= i + di < n and 0 <= j + dj < n and (b[i + di][j + dj] == 'o')]) % 2 == 0
print('YES' if ans else 'NO')
