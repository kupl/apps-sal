n, m, k = map(int, input().split())
seen = [0 for _ in range(m)]

for i in range(n):
    S = list(input())
    for j in range(m):
        if S[j] == 'U' and not i & 1:
            seen[j] += 1
        elif S[j] == 'L' and j - i >= 0:
            seen[j - i] += 1
        elif S[j] == 'R' and j + i < m:
            seen[j + i] += 1

print(*seen, sep=" ")
