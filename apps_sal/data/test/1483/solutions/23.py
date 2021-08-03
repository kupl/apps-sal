
n = int(input())
pointers = list([int(x) - 1 for x in input().split()])
results = []

for i in range(n):
    visited = [False] * n
    while not visited[i]:
        visited[i] = True
        i = pointers[i]
    results.append(str(i + 1))

print(' '.join(results))
