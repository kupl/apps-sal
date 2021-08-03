n = int(input())
x = list(map(int, input().split()))

ans = n * 100**2
for p in range(101):
    ans = min(ans, sum([(xi - p)**2 for xi in x]))
print(ans)
