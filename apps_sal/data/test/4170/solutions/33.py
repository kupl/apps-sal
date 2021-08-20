n = int(input())
h = list(map(int, input().split()))
ans = cnt = 0
for i in range(n - 1):
    if h[i] >= h[i + 1]:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
print(max(ans, cnt))
