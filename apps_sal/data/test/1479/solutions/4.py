(n, m, k) = map(int, input().split())
ans = [0] * m
for i in range(n):
    field = input()
    for j in range(m):
        if field[j] == 'U' and i % 2 == 0:
            ans[j] += 1
        elif field[j] == 'L' and j >= i:
            ans[j - i] += 1
        elif field[j] == 'R' and j + i < m:
            ans[j + i] += 1
print(' '.join(map(str, ans)))
