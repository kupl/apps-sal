n = int(input())
a = list(map(int, input().split()))
ans = 1
cnt = 1
for i in range(1, n):
    if a[i - 1] * 2 >= a[i]:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1
print(max(ans, cnt))

