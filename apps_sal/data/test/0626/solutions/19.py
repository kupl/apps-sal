n = int(input())
lst = list(map(int, input().split()))
ans = 0
zap = 0
used = [False] * (n)
while zap != n:
    if zap != 0:
        ans += 1
    for i in range(n):
        if not used[i] and zap >= lst[i]:
            used[i] = True
            zap += 1

    if zap == n:
        break
    ans += 1
    for i in range(n - 1, -1, -1):
        if not used[i] and zap >= lst[i]:
            used[i] = True
            zap += 1

print(ans)
