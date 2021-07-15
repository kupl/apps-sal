t = int(input())
for case in range(t):
    n = int(input())
    ans = [2 * n + 2 * i + 2 for i in range(n)]
    print(*ans)
