(n, m) = list(map(int, input().split()))
v = list(map(int, input().split()))
cnt = [0 for i in range(0, m + 1)]
for x in v:
    cnt[x] += 1
sol = n * (n - 1) // 2
for x in cnt:
    sol -= x * (x - 1) // 2
print(sol)
