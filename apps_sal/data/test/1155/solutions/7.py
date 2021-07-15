n,m = list(map(int, input().strip().split()))
best = 10**9

for _ in range(n):
    a,b = list(map(int, input().strip().split()))
    best = min(best, m*(a/b))

print(best)

