n = int(input())
odds = [[False] * n for _ in range(n)]
numbers = [[None] * n for _ in range(n)]
for i in range(n // 2):
    for j in range(n):
        mid = n // 2
        if mid - i <= j <= mid + i:
            odds[i][j] = True
odds[n // 2] = [True] * n
for i in range(n // 2 + 1, n):
    for j in range(n):
        mid = n // 2
        dist = n - i - 1
        if mid - dist <= j <= mid + dist:
            odds[i][j] = True
(odd, even) = (1, 2)
for i in range(n):
    for j in range(n):
        if odds[i][j]:
            numbers[i][j] = odd
            odd += 2
        else:
            numbers[i][j] = even
            even += 2
print('\n'.join((' '.join(map(str, row)) for row in numbers)))
