from collections import Counter

n = int(input())

grid = []
for i in range(n):
    grid.append(input())

print(Counter(grid).most_common(1)[0][1])
