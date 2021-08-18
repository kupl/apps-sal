
n, c = map(int, input().split())

ans = [0] * 500001
res = 0

for i in map(int, input().split()):
    ans[i] = max(ans[i], ans[c])
    ans[i] += 1
    res = max(res, ans[i] - ans[c])

print(res + ans[c])
