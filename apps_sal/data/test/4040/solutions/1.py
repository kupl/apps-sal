import sys
n, m, d = list(map(int, input().split()))
c = list(map(int, input().split()))

cur = 0
for p in range(m):
    cur += d
    cur += c[p] - 1
if cur < n + 1 - d:
    print('NO')
    return
res = [0] * n
cur = n - 1
for p in range(m - 1, -1, -1):
    for j in range(c[p]):
        res[cur] = p + 1
        cur -= 1
cur = 0
while cur < n + 1:
    cur += d
    if cur >= n + 1:
        break
    if res[cur - 1] == 0:
        idx = -1
        for j in range(cur, len(res)):
            if res[j] != 0:
                idx = j
                break
        cnt = 1
        for j in range(idx + 1, len(res)):
            if res[j] == res[idx]:
                cnt += 1
        num = res[idx]
        for j in range(cnt):
            res[cur + j - 1] = num
            res[idx + j] = 0
    while cur < len(res) and res[cur] > 0:
        cur += 1
print("YES")
print(' '.join(str(x) for x in res))
        

