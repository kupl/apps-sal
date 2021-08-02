n = int(input())
a = list(map(int, input().split()))
ans = 10**10
for i in range(min(a), max(a) + 1):
    cnt = 0
    for j in range(n):
        cnt += (a[j] - i) ** 2
    ans = min(ans, cnt)
print(ans)
