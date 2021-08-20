(n, m) = [int(c) for c in input().split()]
lines = []
for i in range(n):
    lines.append(input())
f = 0
for i in range(n - 1):
    for j in range(m - 1):
        s = set()
        s.add(lines[i][j])
        s.add(lines[i + 1][j])
        s.add(lines[i][j + 1])
        s.add(lines[i + 1][j + 1])
        if 'f' in s and 'a' in s and ('c' in s) and ('e' in s):
            f += 1
print(f)
