(n, x) = map(int, input().split())
mini = 1000
amount = 0
ans = 0
for _ in range(n):
    m = int(input())
    mini = min(mini, m)
    x -= m
    ans += 1
ans += x // mini
print(ans)
