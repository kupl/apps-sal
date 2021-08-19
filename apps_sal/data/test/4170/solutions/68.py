n = int(input())
h = list(map(int, input().split()))
tmp = 0
ans = 0
for i in range(n - 1):
    if h[i] >= h[i + 1]:
        tmp += 1
    else:
        ans = max(ans, tmp)
        tmp = 0
ans = max(ans, tmp)
print(ans)
