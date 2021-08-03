n = int(input())
deg = [0 for _ in range(n)]
for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    deg[a] += 1
    deg[b] += 1
ans = 0
for x in deg:
    ans += x * (x - 1) // 2
print(ans)
