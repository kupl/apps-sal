n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 10 ** 10
for x in range(a[0], a[-1] + 1):
    tmp = 0
    for i in range(n):
        tmp += (a[i] - x) ** 2
    ans = min(ans, tmp)
print(ans)
