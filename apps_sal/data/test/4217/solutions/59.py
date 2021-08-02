n, m = map(int, input().split())
k_a = [list(map(int, input().split())) for _ in range(n)]

ans = {}
for a in k_a:
    for i in a[1:]:
        if i in ans.keys():
            ans[i] += 1
        else:
            ans[i] = 1
print(sum([1 for i, v in ans.items() if v == n]))
