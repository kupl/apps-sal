n = int(input())

lines = [0 for _ in range(101)]

for _ in range(n):
    l, *line = list(map(int, input().strip().split()))
    for v in line:
        lines[v] += 1

maxv = 0
ans = []
for index, line in enumerate(lines):
    if line > maxv:
        ans = [index]
        maxv = line
    elif line == maxv:
        ans.append(index)

print(*ans)
