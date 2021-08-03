n = int(input())
up = list(map(int, input().split()))
dw = list(map(int, input().split()))
ans = up[0] + sum(dw)
tmp = up[0] + sum(dw)
for i in range(1, n):
    tmp = tmp + up[i] - dw[i - 1]
    ans = max(tmp, ans)
print(ans)
