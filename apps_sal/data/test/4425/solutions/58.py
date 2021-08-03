n, k = map(int, input().split())
ans = 0
for i in range(1, n + 1):
    tokuten = i
    tmp = 1 / n
    while tokuten < k:
        tokuten *= 2
        tmp = tmp / 2
    # print(tmp)
    ans += tmp
print(ans)
