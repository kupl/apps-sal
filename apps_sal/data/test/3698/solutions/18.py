R = lambda: map(int, input().split())
mod = 10 ** 9 + 7
maxn = 1001
c = [[0 for j in range(maxn)] for i in range(maxn)]
for i in range(maxn):
    c[i][0] = 1
for i in range(1, maxn):
    for j in range(i + 1):
        c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % mod
arr = list(map(int, input()))
k = int(input())
if k == 0:
    print(1 if arr.count(1) else 0)
    return
ops = [0] * (maxn + 1)
ans = 0
for i in range(2, maxn):
    cnt = bin(i).count('1')
    ops[i] = ops[cnt] + 1
for i in range(1, maxn):
    if ops[i] == k - 1:
        oc = i
        for j, x in enumerate(arr):
            if x and oc >= 0:
                ans = (ans + c[len(arr) - j - 1][oc]) % mod
                oc -= 1
        ans = (ans + 1) % mod if arr.count(1) == i else ans
if k == 1:
    ans = (ans + mod - 1) % mod
print(ans)
