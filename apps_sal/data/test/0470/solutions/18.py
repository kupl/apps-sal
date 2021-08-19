n = list(map(int, input().split()))
n.sort()
ans = 0
for i in range(len(n) - 1):
    if n[i] == n[i + 1]:
        ans = max(n[i] + n[i + 1], ans)
for i in range(len(n) - 2):
    if n[i] == n[i + 1] and n[i] == n[i + 2]:
        ans = max(n[i] + n[i + 1] + n[i + 2], ans)
print(sum(n) - ans)
