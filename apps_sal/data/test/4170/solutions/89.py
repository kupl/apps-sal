n = int(input())
L = list(map(int, input().split()))
ans = 0
cnt = 0
for i in range(n - 1):
    if L[i + 1] <= L[i]:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
ans = max(ans, cnt)
print(ans)
