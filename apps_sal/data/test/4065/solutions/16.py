n = int(input())
a = list(map(int, input().split()))
cnt = 1
ans = 1
for i in range(1, n):
    if a[i] > 2 * a[i - 1]:
        ans = max(ans, cnt)
        cnt = 1
    else:
        cnt += 1
ans = max(ans, cnt)
print(ans)
