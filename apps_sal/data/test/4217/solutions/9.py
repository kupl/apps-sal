(n, m) = map(int, input().split())
ans = [0] * m
for i in range(n):
    k = list(map(int, input().split()))
    for j in range(1, m + 1):
        if j in k[1:]:
            ans[j - 1] += 1
print(ans.count(n))
