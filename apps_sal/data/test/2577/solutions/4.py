def solve(n, m):
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(m):
            if (row[j] + i + j) % 2:
                row[j] += 1
        print(*row)


t = int(input())
for i in range(t):
    n, m = list(map(int, input().split()))
    solve(n, m)
