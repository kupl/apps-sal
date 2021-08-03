n = int(input())
em = [0] * n
mx = [0] * n
for k in range(n):
    ar = list(map(int, input().split()))
    em[k] = (ar[0])
    mx[k] = (max(ar[1:]))
ans = 0
maxx = max(mx)
for k in range(n):
    ans += em[k] * (maxx - mx[k])
print(ans)
