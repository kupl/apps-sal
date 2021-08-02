N, D = map(int, input().split())

monitor, ans = 0, 0
while monitor < N:
    monitor += 2 * D + 1
    ans += 1
print(ans)
