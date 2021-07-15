t = int(input())

for _ in range(t):
    n = int(input())
    seen = [-1] * (n+1)
    ans = n*n
    for i, v in enumerate(map(int, input().split())):
        if seen[v] != -1:
            ans = min(ans, i - seen[v] + 1)
        seen[v] = i
    print(ans if ans != n*n else -1)

