n, d = map(int, input().split())
lists = []
for i in range(n):
    lis = list(map(int, input().split()))
    lists.append(lis)
cnt = 0
for i in range(0, n - 1):
    for j in range(i + 1, n):
        ans = 0
        for k in range(d):
            x = (lists[i][k] - lists[j][k])**2
            ans += x
        ans = ans**(1 / 2)
        y = ans.is_integer()
        if y == True:
            cnt += 1
print(cnt)
