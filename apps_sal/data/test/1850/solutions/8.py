(n, d) = list(map(int, input().strip().split()))
pre = list(map(int, input().strip().split()))
nxt = list(map(int, input().strip().split()))
pre[d - 1] += nxt[0]
nxt[0] = -10
k = n
l = 1
ans = 0
for i in range(d - 2, -1, -1):
    for j in range(l, k):
        l += 1
        if pre[i] + nxt[j] <= pre[d - 1]:
            ans += 1
            break
    if l == n:
        break
print(d - ans)
