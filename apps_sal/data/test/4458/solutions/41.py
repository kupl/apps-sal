N = int(input())
P = list(map(int, input().split()))
ans = 0
mini = 10 ** 6
for p in P:
    if p <= mini:
        mini = p
        ans += 1
print(ans)
