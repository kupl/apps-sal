n = int(input())
a = list(map(int, input().split()))
cnt = 0
ans = 0
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        cnt += 1
    else:
        ans = max(cnt, ans)
        cnt = 0
ans = max(ans, cnt)
print(ans + 1)
