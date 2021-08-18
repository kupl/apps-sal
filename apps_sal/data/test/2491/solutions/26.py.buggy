import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(m)]
dist = [-float("inf")] * (n + 1)
dist[1] = 0
for i in range(n):
    for a, b, c in ABC:
        if dist[b] < dist[a] + c:
            if i == n - 1 and b == n:
                print("inf")
                return
            dist[b] = dist[a] + c
ans = dist[n]
print(ans)
