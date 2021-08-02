import sys
sys.setrecursionlimit(1919810)


def dfs(i):
    if i == 2 * n + 1:
        nonlocal ans
        ans = "Yes"
        return
    if ans == "No":
        if y[i] == 0:
            for k in range(1, n):
                if ok(k, i):
                    dfs(i + 2 * k)
        else:
            if ok(y[i], i):
                dfs(i + 2 * y[i])
    return


def ok(k, i):
    if k + i >= 2 * n + 1:
        return 0
    f = 1
    for l in range(k):
        if k + i + l >= 2 * n + 1:
            f = 0
            break
        if x[i + l] == 2 or x[k + i + l] == 1:
            f = 0
            break
        if not (y[i + l] == 0 or y[i + l] == k):
            f = 0
            break
        if not z[i + l] == z[k + i + l] and min(z[i + l], z[k + i + l]) >= 1:
            f = 0
            break
    return f


n = int(input())
ans = "Yes"
x = [0] * (2 * n + 2)
y = [0] * (2 * n + 2)
z = [0] * (2 * n + 2)
for i in range(1, n + 1):
    a, b = map(int, input().split())
    if a >= b and not (a == -1 or b == -1):
        ans = "No"
    if not (x[a] == 0 and x[b] == 0):
        ans = "No"
    if not a == -1:
        x[a] = 1
        z[a] = i
    if not b == -1:
        x[b] = 2
        z[b] = i
    if not (a == -1 or b == -1):
        y[a] = b - a
if ans == "No":
    print(ans)
    return
ans = "No"
dfs(1)
print(ans)
