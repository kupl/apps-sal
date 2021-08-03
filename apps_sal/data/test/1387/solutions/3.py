n, t = map(int, input().split())
a = list(map(int, input().split()))
can = [0 for _ in range(n)]
can[0] = 1
for i in range(n - 1):
    if can[i]:
        can[i + a[i]] = 1
print("YES" if can[t - 1] else "NO")
