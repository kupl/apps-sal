n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
for b in range(n):
    closed = [b + i * k for i in range(-n, n)]
    closed = set(c for c in closed if 0 <= c < n)
    test = sum(a[i] == -1 and i not in closed for i in range(n))
    play = sum(a[i] == 1 and i not in closed for i in range(n))
    ans = max(ans, abs(test - play))

print(ans)

