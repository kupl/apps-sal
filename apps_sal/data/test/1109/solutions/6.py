n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
for i in range(k):
    c = [0] * 2
    for j in range(i, n, k):
        c[a[j] - 1] += 1
    ans += min(c)
print(ans)
