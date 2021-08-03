n, x, y = map(int, input().split())
counter = {i + 1: 0 for i in range(n - 1)}

for i in range(n - 1):
    for j in range(i + 1, n):
        k = min(j - i, abs(x - 1 - i) + abs(y - 1 - j) + 1)
        counter[k] += 1

print(*[counter[i + 1] for i in range(n - 1)], sep='\n')
