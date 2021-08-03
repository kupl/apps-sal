def gen(k, n, p):
    if k == n:
        ans.append(p)
        return
    gen(k + 1, n, p + [1])
    gen(k + 1, n, p + [0])


n, l, r, x = list(map(int, input().split()))
m = list(map(int, input().split()))
ans = []
count = 0
gen(0, n, [])
for i in range(len(ans)):
    now = []
    for j in range(len(ans[i])):
        if ans[i][j] == 1:
            now.append(m[j])
    now.sort()
    sum = 0
    for i in now:
        sum += i
    if len(now) > 0:
        if now[-1] - now[0] >= x and sum >= l and sum <= r:
            count += 1
print(count)
