n = int(input())
h = list(map(int, input().split()))
ans = 0
cnt = 0
for i in range(n - 1):
    if h[i] >= h[i + 1]:
        cnt += 1
    else:
        if cnt > ans:
            ans = cnt
        cnt = 0
else:
    if cnt > ans:
        ans = cnt
print(ans)
