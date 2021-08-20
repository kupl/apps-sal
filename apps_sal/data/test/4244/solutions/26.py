N = int(input())
X = list(map(int, input().split()))
max_x = max(X)
min_x = min(X)
min_y = 9999999999
for p in range(min_x, max_x + 1):
    y = sum([(x - p) ** 2 for x in X])
    if y < min_y:
        min_y = y
print(min_y)
