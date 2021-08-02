n = int(input())
s = list(map(int, input().split()))

ans = 0
for step in range(1, n):
    now = 0
    for i, j in zip(list(range(0, n, step)), list(range(n - 1, -1, -step))):
        if i == j or i - j == step or j < step:
            break
        now += s[i] + s[j]
        ans = max(ans, now)
print(ans)
